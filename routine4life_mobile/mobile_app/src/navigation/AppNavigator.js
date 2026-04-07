import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createDrawerNavigator } from '@react-navigation/drawer';

// Importación de pantallas y componentes
import HomeScreen from '../screens/HomeScreen';
import LoginScreen from '../screens/LoginScreen';
import RegisterScreen from '../screens/RegisterScreen';
import RegisterPasswordScreen from '../screens/RegisterPasswordScreen';
import RecoverPasswordStep1Screen from '../screens/RecoverPasswordStep1Screen';
import RecoverPasswordStep2Screen from '../screens/RecoverPasswordStep2Screen';

// Importar tu componente personalizado
import CustomDrawer from '../components/CustomDrawer'; 

const Stack = createStackNavigator();
const Drawer = createDrawerNavigator();

// --- Navegador Lateral (Drawer) ---
const DrawerNavigator = () => {
  return (
    <Drawer.Navigator
      drawerContent={(props) => <CustomDrawer {...props} />}
      screenOptions={{
        headerShown: false, // Usamos tu propio header de HomeScreen
        drawerStyle: { width: '80%' },
      }}
    >
      {/* 1. HomeScreen DEBE estar aquí adentro para tener acceso al menú */}
      <Drawer.Screen name="Home" component={HomeScreen} />
      
      {/* Si creas ProfileScreen u otras, agrégalas aquí abajo */}
      {/* <Drawer.Screen name="Profile" component={ProfileScreen} /> */}
    </Drawer.Navigator>
  );
};

// --- Navegador Principal ---
const AppNavigator = () => {
  return (
    <NavigationContainer>
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
        
        {/* 2. Reemplazamos el componente de la pantalla por el DrawerNavigator */}
        {/* Nota: Le cambié el nombre a "Main" en el Stack para evitar conflictos 
            con el "Home" que ahora vive dentro del Drawer. Al hacer login, 
            deberás navegar hacia "Main". */}
        <Stack.Screen name="Main" component={DrawerNavigator} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default AppNavigator;