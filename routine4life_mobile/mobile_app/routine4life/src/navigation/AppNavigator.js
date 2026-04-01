import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { createStackNavigator } from '@react-navigation/stack';

// Importación de pantallas y componentes
import HomeScreen from '../screens/HomeScreen';
import LoginScreen from '../screens/LoginScreen';
import RegisterScreen from '../screens/RegisterScreen';
import RegisterPasswordScreen from '../screens/RegisterPasswordScreen';
import RecoverPasswordStep1Screen from '../screens/RecoverPasswordStep1Screen';
import RecoverPasswordStep2Screen from '../screens/RecoverPasswordStep2Screen';
import CustomDrawer from '../components/CustomDrawer';

const Drawer = createDrawerNavigator();
const Stack = createStackNavigator();

const AppDrawer = () => {
  return (
    <Drawer.Navigator
      drawerContent={(props) => <CustomDrawer {...props} />}
      screenOptions={{
        headerShown: false,
        drawerType: 'front',
        drawerStyle: {
          backgroundColor: '#F5F0E8',
          width: '80%',
          borderTopRightRadius: 60,
          borderBottomRightRadius: 60,
          // Añadimos esto para asegurar que el contenido respete el radio
          overflow: 'hidden', 
        },
        overlayColor: 'rgba(0,0,0,0.5)',
        // Importante para el rendimiento en Android/Expo Go
        drawerHideStatusBarOnOpen: false, 
      }}
    >
      <Drawer.Screen 
        name="Home" 
        component={HomeScreen} 
        options={{ title: 'Mis registros' }} 
      />
    </Drawer.Navigator>
  );
};

const AppNavigator = () => {
  return (
    <NavigationContainer>
      {/* Usamos detachPreviousScreen en false solo si notas parpadeos, 
          pero por defecto la config actual es óptima. 
      */}
      <Stack.Navigator 
        screenOptions={{ headerShown: false }} 
        initialRouteName="Login"
      >
        {/* Flujo de Autenticación */}
        <Stack.Screen name="Login" component={LoginScreen} />
        <Stack.Screen name="Register" component={RegisterScreen} />
        <Stack.Screen name="RegisterPassword" component={RegisterPasswordScreen} />
        <Stack.Screen name="RecoverPasswordStep1" component={RecoverPasswordStep1Screen} />
        <Stack.Screen name="RecoverPasswordStep2" component={RecoverPasswordStep2Screen} />
        
        {/* Flujo Interno de la App */}
        <Stack.Screen name="AppDrawer" component={AppDrawer} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default AppNavigator;