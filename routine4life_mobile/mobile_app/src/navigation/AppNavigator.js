import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createDrawerNavigator } from '@react-navigation/drawer'; // 1. Importar Drawer

// Importación de pantallas y componentes
import HomeScreen from '../screens/HomeScreen';
import LoginScreen from '../screens/LoginScreen';
import RegisterScreen from '../screens/RegisterScreen';
import RegisterPasswordScreen from '../screens/RegisterPasswordScreen';
import RecoverPasswordStep1Screen from '../screens/RecoverPasswordStep1Screen';
import RecoverPasswordStep2Screen from '../screens/RecoverPasswordStep2Screen';

// 2. Importar tu componente personalizado
import CustomDrawer from '../components/CustomDrawer'; 

const Stack = createStackNavigator();
const Drawer = createDrawerNavigator();

// --- NUEVO: Navegador Lateral ---
const DrawerNavigator = () => {
  return (
    <Drawer.Navigator
      drawerContent={(props) => <CustomDrawer {...props} />}
      screenOptions={{
        headerShown: false, // Usamos tu propio header de HomeScreen
        drawerStyle: { width: '80%' },
      }}
    >
      <Drawer.Screen name="HomeScreen" component={HomeScreen} />
      {/* Aquí puedes agregar más pantallas que deban tener el menú lateral,
         por ejemplo: Drawer.Screen name="Profile" component={ProfileScreen} 
      */}
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
        
        {/* 3. Flujo Interno: Reemplazamos HomeScreen por el DrawerNavigator */}
        <Stack.Screen name="MainDrawer" component={DrawerNavigator} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default AppNavigator;