import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

// Importación de pantallas y componentes
import HomeScreen from '../screens/HomeScreen';
import LoginScreen from '../screens/LoginScreen';
import RegisterScreen from '../screens/RegisterScreen';
import RegisterPasswordScreen from '../screens/RegisterPasswordScreen';
import RecoverPasswordStep1Screen from '../screens/RecoverPasswordStep1Screen';
import RecoverPasswordStep2Screen from '../screens/RecoverPasswordStep2Screen';

const Stack = createStackNavigator();

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
        
        {/* Flujo Interno de la App */}
        <Stack.Screen name="Home" component={HomeScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default AppNavigator;