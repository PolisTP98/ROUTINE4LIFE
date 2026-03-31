import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';

// Importación de pantallas y componentes
import HomeScreen from '../screens/HomeScreen';
import CustomDrawer from '../components/CustomDrawer';
import { COLORS } from '../styles/theme';

const Drawer = createDrawerNavigator();

const AppNavigator = () => {
  return (
    <NavigationContainer>
      <Drawer.Navigator
        // Usamos el componente personalizado para el diseño del menú lateral
        drawerContent={(props) => <CustomDrawer {...props} />}
        screenOptions={{
          headerShown: false, // Ocultamos el header por defecto de la librería para usar el tuyo personalizado
          drawerType: 'front', // El menú aparece por encima de la pantalla
          drawerStyle: {
            backgroundColor: '#F5F0E8', // Fondo beige
            width: '80%', // Ancho del menú
            borderTopRightRadius: 60, // Curva superior derecha
            borderBottomRightRadius: 60, // Curva inferior derecha
          },
          overlayColor: 'rgba(0,0,0,0.5)', // Color de fondo al estar abierto
        }}
      >
        {/* Definición de rutas */}
        <Drawer.Screen 
          name="Home" 
          component={HomeScreen} 
          options={{ title: 'Mis registros' }} 
        />
        
        {/* Aquí puedes añadir más pantallas conforme las crees:
        <Drawer.Screen name="CitasMedicas" component={CitasScreen} />
        <Drawer.Screen name="Notificaciones" component={NotificacionesScreen} /> 
        */}
      </Drawer.Navigator>
    </NavigationContainer>
  );
};

export default AppNavigator;