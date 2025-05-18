import folium
import webbrowser
import os
from src.controllers.booking_controller import is_booking_active
from src.controllers.global_dicts import bookings, cars

def generate_map(filename="car_tracking_map.html"):
    """
    Gera um mapa com todas as reservas de carros que possuem coordenadas
    """
    # Filtrar apenas reservas com coordenadas válidas
    valid_bookings = {booking_id: booking for booking_id, booking in bookings.items() 
                     if booking.latitude is not None and booking.longitude is not None}
    
    if not valid_bookings:
        print("No booking with valid coordinates found.")
        # Se não houver reservas válidas, criar um mapa centrado em São Paulo
        map_center = [-23.5505, -46.6333]  # São Paulo coordinates
        map = folium.Map(location=map_center, zoom_start=12)
    else:
        # Usar a localização da primeira reserva como centro do mapa
        first_booking_id = next(iter(valid_bookings))
        first_booking = valid_bookings[first_booking_id]
        map_center = [first_booking.latitude, first_booking.longitude]
        map = folium.Map(location=map_center, zoom_start=12)
    
    # Adicionar cada reserva ao mapa
    for booking_id, booking in valid_bookings.items():
        # Determinar cor com base no status da reserva
        is_active = is_booking_active(booking)
        marker_color = 'blue' if is_active else 'red'
        
        # Obter informações do veículo
        car_info = ""
        car = cars.get(booking.car_id)
        if car:
            car_info = f"""
            <b>Marca:</b> {car.brand}<br>
            <b>Modelo:</b> {car.model}<br>
            """
            
        # Configurar o ícone personalizado
        icon_path = os.path.abspath('src/utils/guru.png')
        try:
            icon = folium.features.CustomIcon(
                    icon_image=icon_path,
                    icon_size=(30, 30),
                    icon_anchor=(15, 15),
                    popup_anchor=(0, -15)
                )
           
        except Exception as e:
            print(f"Error loading custom icon: {e}")
            icon = folium.Icon(color=marker_color, icon='car', prefix='fa')
        
        # Adicionar marcador para a reserva
        popup_text = f"""
        <b>Reserva ID:</b> {booking_id}<br>
        <b>Carro ID:</b> {booking.car_id}<br>
        {car_info}
        <b>Cliente:</b> {booking.customer_email}<br>
        <b>Status:</b> {'Em uso' if is_active else 'Reservado'}<br>
        <b>Início:</b> {booking.start_date}<br>
        <b>Fim:</b> {booking.end_date}<br>
        """
        
        folium.Marker(
            [booking.latitude, booking.longitude],
            popup=folium.Popup(popup_text, max_width=300),
            icon=icon
        ).add_to(map)
    
    # Salvar o mapa
    map_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), filename)
    map.save(map_path)
    
    print(f"Mapa salvo em: {map_path}")
    return map_path

def show_map():
    """
    Gera e abre o mapa no navegador padrão
    """
    map_path = generate_map()
    webbrowser.open('file://' + os.path.realpath(map_path))

def generate_car_map(car_id, filename="car_map.html"):
    """
    Gera um mapa para um carro específico
    """
    # Filtrar apenas reservas do carro especificado com coordenadas válidas
    car_bookings = {booking_id: booking for booking_id, booking in bookings.items() 
                   if booking.car_id == car_id and 
                   booking.latitude is not None and booking.longitude is not None}
    
    if not car_bookings:
        print(f"No booking with valid coordinates found for car {car_id}.")
        return None
    
    # Usar a localização da primeira reserva como centro do mapa
    first_booking_id = next(iter(car_bookings))
    first_booking = car_bookings[first_booking_id]
    map = folium.Map(location=[first_booking.latitude, first_booking.longitude], zoom_start=12)
    
    # Adicionar cada reserva ao mapa
    for booking_id, booking in car_bookings.items():
        # Determinar cor com base no status da reserva
        is_active = is_booking_active(booking)
        marker_color = 'blue' if is_active else 'red'
        
        # Obter informações do veículo
        car = cars.get(car_id)
        car_info = f"""
        <b>Marca:</b> {car.brand if car else 'N/A'}<br>
        <b>Modelo:</b> {car.model if car else 'N/A'}<br>
        """
        
        # Adicionar marcador para a reserva
        popup_text = f"""
        <b>Reserva ID:</b> {booking_id}<br>
        <b>Cliente:</b> {booking.customer_email}<br>
        <b>Status:</b> {'Em uso' if is_active else 'Reservado'}<br>
        <b>Início:</b> {booking.start_date}<br>
        <b>Fim:</b> {booking.end_date}<br>
        {car_info}
        """
        
        # Na função generate_car_map, substitua o trecho do marcador por:
        
        # Configurar o ícone personalizado
        icon_path = os.path.abspath('src/utils/guru.png')
        try:
            icon = folium.features.CustomIcon(
                icon_image=icon_path,
                icon_size=(30, 30),
                icon_anchor=(15, 15),
                popup_anchor=(0, -15)
            )
        except Exception as e:
            print(f"Error loading custom icon: {e}")
            icon = folium.Icon(color='red', icon='car', prefix='fa')
            
        folium.Marker(
            [booking.latitude, booking.longitude],
            popup=folium.Popup(popup_text, max_width=300),
            icon=icon
        ).add_to(map)
    
    # Salvar o mapa
    map_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), filename)
    map.save(map_path)
    
    print(f"Mapa do carro {car_id} salvo em: {map_path}")
    return map_path

def show_car_map():
    """
    Gera e abre o mapa de um carro específico no navegador padrão
    """

    car_id = int(input("\nEnter car ID to track: "))
    print(f"\nGenerating map for car {car_id}...")
    map_path = generate_car_map(car_id)
    if map_path:
        webbrowser.open('file://' + os.path.realpath(map_path))
        print("\nMap opened in your browser.")
