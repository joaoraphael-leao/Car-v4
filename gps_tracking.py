import folium
import webbrowser
import os
import datetime
import car_request  
import car_management

def is_request_active(request):
    """
    Verifica se a requisição está ativa (já começou mas ainda não terminou)
    """
    now = datetime.datetime.now()
    if request['start_date'] and request['end_date']:
        return request['start_date'] <= now <= request['end_date']
    return False

def generate_map_from_requests(filename="car_tracking_map.html"):
    """
    Gera um mapa com todas as requisições de carros
    """
    # Filtrar apenas requisições com coordenadas válidas
    valid_requests = {car_id: req for car_id, req in car_request.requests.items() 
                     if req.get('latitude') and req.get('longitude')}
    
    if not valid_requests:
        print("Nenhuma requisição com coordenadas válidas encontrada.")
        # Se não houver requisições válidas, criar um mapa centrado em São Paulo
        map = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)
        map_path = os.path.join(os.path.dirname(__file__), filename)
        map.save(map_path)
        return map_path
    
    # Usar a localização da primeira requisição como centro do mapa
    first_car_id = next(iter(valid_requests))
    first_request = valid_requests[first_car_id]
    map = folium.Map(location=[first_request['latitude'], first_request['longitude']], zoom_start=12)
    
    # Adicionar cada requisição ao mapa
    for car_id, request in valid_requests.items():
        # Determinar cor com base no status da requisição
        is_active = is_request_active(request)
        marker_color = 'blue' if is_active else 'red'
        
        # Obter informações do veículo
        car_info = ""
        if car_id in car_management.car_list:
            car = car_management.car_list[car_id]
            car_info = f"""
            <b>Marca:</b> {car.brand}<br>
            <b>Modelo:</b> {car.model}<br>
            <b>Cor:</b> {car.color}<br>
            """
        
        # Adicionar marcador para a requisição
        popup_text = f"""
        <b>Carro ID:</b> {car_id}<br>
        {car_info}
        <b>Cliente:</b> {request['nickname']}<br>
        <b>Status:</b> {'Em uso' if is_active else 'Reservado (não iniciado)'}<br>
        <b>Endereço:</b> {request['address']}<br>
        <b>Início:</b> {request['start_date'].strftime('%d/%m/%Y')}<br>
        <b>Fim:</b> {request['end_date'].strftime('%d/%m/%Y')}<br>
        """
        
        folium.Marker(
            [request['latitude'], request['longitude']],
            popup=folium.Popup(popup_text, max_width=300),
            icon=folium.Icon(color=marker_color, icon='car', prefix='fa')
        ).add_to(map)
    
    # Salvar o mapa
    map_path = os.path.join(os.path.dirname(__file__), filename)
    map.save(map_path)
    
    return map_path

def generate_all_cars_map(filename="all_cars_map.html"):
    """
    Gera um mapa com todos os carros do sistema
    """
    if not car_management.car_list:
        print("Nenhum carro cadastrado no sistema.")
        return None
    
    # Usar São Paulo como centro do mapa
    map = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)
    
    # Adicionar cada carro ao mapa
    for car_id, car in car_management.car_list.items():
        # Verificar se o carro está em alguma requisição
        in_request = car_id in car_request.requests
        
        # Obter coordenadas do carro (da requisição ou padrão)
        latitude, longitude = -23.5505, -46.6333  # Coordenadas padrão (São Paulo)
        address = "Localização não especificada"
        
        if in_request and 'latitude' in car_request.requests[car_id] and 'longitude' in car_request.requests[car_id]:
            latitude = car_request.requests[car_id]['latitude']
            longitude = car_request.requests[car_id]['longitude']
            address = car_request.requests[car_id]['address']
        
        # Determinar cor com base na disponibilidade
        is_available = car.available.lower() == 'yes'
        marker_color = 'green' if is_available else 'red'
        
        # Adicionar marcador para o carro
        popup_text = f"""
        <b>Carro ID:</b> {car_id}<br>
        <b>Marca:</b> {car.brand}<br>
        <b>Modelo:</b> {car.model}<br>
        <b>Cor:</b> {car.color}<br>
        <b>Disponível:</b> {'Sim' if is_available else 'Não'}<br>
        <b>Preço/dia:</b> R${car.price_day}<br>
        <b>Endereço:</b> {address}<br>
        """
        
        folium.Marker(
            [latitude, longitude],
            popup=folium.Popup(popup_text, max_width=300),
            icon=folium.Icon(color=marker_color, icon='car', prefix='fa')
        ).add_to(map)
    
    # Salvar o mapa
    map_path = os.path.join(os.path.dirname(__file__), filename)
    map.save(map_path)
    
    return map_path

def open_map_in_browser(map_path):
    """
    Abre o mapa no navegador padrão
    """
    if map_path and os.path.exists(map_path):
        webbrowser.open('file://' + os.path.abspath(map_path))
        return True
    return False

def gps_tracking_main():
    """
    Função principal para o menu de GPS tracking
    """
    user_input = ''
    
    while user_input != '4':
        print("GPS Tracking Menu\n")
        print("1. View All Cars Map")
        print("2. View Car Tracking Map")
        print("3. Update Car Location")
        print("4. Exit")
        
        user_input = input("\n")
        os.system('cls')
        
        if user_input == '1':
            map_path = generate_all_cars_map()
            if map_path:
                print(f"Mapa gerado em: {map_path}")
                open_map_in_browser(map_path)
            else:
                print("Não foi possível gerar o mapa.")
        
        elif user_input == '2':
            map_path = generate_map_from_requests()
            if map_path:
                print(f"Mapa gerado em: {map_path}")
                open_map_in_browser(map_path)
            else:
                print("Não foi possível gerar o mapa.")
        
        elif user_input == '3':
            car_id = input("Insert the ID of the car to update location\n")
            
            if car_id in car_request.requests:
                address = input("Insert the new address\n")
                
                try:
                    from geopy.geocoders import Nominatim
                    geolocator = Nominatim(user_agent="car_rental_system")
                    location = geolocator.geocode(address)
                    
                    if location:
                        latitude = location.latitude
                        longitude = location.longitude
                        
                        car_request.requests[car_id]['address'] = address
                        car_request.requests[car_id]['latitude'] = latitude
                        car_request.requests[car_id]['longitude'] = longitude
                        print(f"Localização atualizada para: {latitude}, {longitude}")
                    else:
                        print("Não foi possível obter coordenadas para o endereço fornecido.")
                except Exception as e:
                    print(f"Erro ao obter coordenadas: {e}")
            else:
                print(f"Carro com ID {car_id} não encontrado nas requisições.")

if __name__ == "__main__":
    gps_tracking_main()