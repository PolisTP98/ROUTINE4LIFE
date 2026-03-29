// src/screens/LoginScreen.js
import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, KeyboardAvoidingView, Platform, ScrollView } from 'react-native';
import { Ionicons } from '@expo/vector-icons'; // Requiere npm install @expo/vector-icons
import { COLORS } from '../styles/theme';

const LoginScreen = ({ navigation }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);
  const [secureTextEntry, setSecureTextEntry] = useState(true);

  // Lógica de habilitación de botón: ambos campos deben tener texto
  const isButtonEnabled = email.trim().length > 0 && password.trim().length > 0;

  const handleLogin = () => {
    // Solo navega si el botón está habilitado
    if (isButtonEnabled) {
      navigation.navigate('Home');
    }
  };

  const handleNotImplemented = (action) => {
    alert(`${action} aún no implementado (Futuro desarrollo)`);
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
    >
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        {/* Título */}
        <View style={styles.headerContainer}>
          <Text style={styles.title}>Iniciar sesión</Text>
        </View>

        {/* Formulario */}
        <View style={styles.formContainer}>
          {/* Campo Correo Electrónico */}
          <TextInput
            style={styles.input}
            placeholder="Correo electrónico"
            placeholderTextColor={COLORS.inputText + '70'} // Color del placeholder un poco más tenue
            value={email}
            onChangeText={setEmail}
            keyboardType="email-address"
            autoCapitalize="none"
          />

          {/* Campo Contraseña */}
          <View style={styles.passwordInputContainer}>
            <TextInput
              style={styles.passwordInput}
              placeholder="Contraseña"
              placeholderTextColor={COLORS.inputText + '70'}
              value={password}
              onChangeText={setPassword}
              secureTextEntry={secureTextEntry}
            />
            <TouchableOpacity onPress={() => setSecureTextEntry(!secureTextEntry)} style={styles.iconContainer}>
              <Ionicons
                name={secureTextEntry ? 'eye-outline' : 'eye-off-outline'}
                size={28} // El icono azul en la imagen parece grande
                color={COLORS.primary} // Azul primary de la paleta
              />
            </TouchableOpacity>
          </View>

          {/* Recordarme - Réplica visual aproximada con Touchables */}
          <TouchableOpacity 
            style={styles.rememberMeContainer}
            onPress={() => setRememberMe(!rememberMe)}
          >
            <View style={[styles.checkbox, rememberMe && styles.checkboxActive]}>
              {rememberMe && <Ionicons name="checkmark" size={12} color={COLORS.background} />}
            </View>
            <Text style={styles.rememberMeText}>Recordarme</Text>
          </TouchableOpacity>
        </View>

        {/* Enlaces y Botón de Acción */}
        <View style={styles.actionContainer}>
          {/* Enlace ¿Olvidaste tu contraseña? */}
          <Text style={styles.linkTextBase}>
            ¿Olvidaste tu contraseña?{' '}
            <Text style={styles.linkTextRed} onPress={() => handleNotImplemented('Reestablecer')}>Reestablecer</Text>
          </Text>

          {/* Botón de Iniciar Sesión con lógica dinámica */}
          <TouchableOpacity
            style={[
              styles.loginButton,
              isButtonEnabled ? styles.loginButtonEnabled : styles.loginButtonDisabled
            ]}
            onPress={handleLogin}
            disabled={!isButtonEnabled}
          >
            <Text style={styles.loginButtonText}>Iniciar sesión</Text>
          </TouchableOpacity>

          {/* Enlace ¿No tienes una cuenta? */}
          <Text style={styles.linkTextBase}>
            ¿No tienes una cuenta?{' '}
            <Text style={styles.linkTextRed} onPress={() => handleNotImplemented('Registrarse')}>Registrarse</Text>
          </Text>
        </View>
      </ScrollView>
    </KeyboardAvoidingView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: COLORS.background, // #F5F0E8
  },
  scrollContainer: {
    flexGrow: 1,
    paddingHorizontal: 30, // Márgenes laterales anchos
    paddingTop: '30%', // Baja el título principal
    alignItems: 'center',
  },
  headerContainer: {
    marginBottom: 60,
  },
  title: {
    fontSize: 55, // Título muy grande y centrado
    fontWeight: 'bold',
    color: COLORS.primary, // #1E3A5F
    textAlign: 'center',
    letterSpacing: 0.5,
  },
  formContainer: {
    width: '100%',
    marginBottom: 80, // Espacio antes de los enlaces
  },
  input: {
    backgroundColor: COLORS.inputBackground, // #D4D4D4
    color: COLORS.inputText, // #4A4A4A
    height: 55,
    borderRadius: 30, // Completamente redondeado
    paddingHorizontal: 25,
    fontSize: 18,
    marginBottom: 15,
  },
  passwordInputContainer: {
    flexDirection: 'row',
    backgroundColor: COLORS.inputBackground, // #D4D4D4
    height: 55,
    borderRadius: 30,
    alignItems: 'center',
    paddingHorizontal: 15,
    marginBottom: 15,
  },
  passwordInput: {
    flex: 1,
    color: COLORS.inputText,
    fontSize: 18,
    paddingHorizontal: 10,
  },
  iconContainer: {
    padding: 10,
  },
  rememberMeContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingLeft: 10, // Alineado un poco con los bordes anchos del input
  },
  // Simulación del checkbox circular gris
  checkbox: {
    width: 20,
    height: 20,
    borderRadius: 10, // Circular
    backgroundColor: '#D4D4D4', // Gris claro visual
    marginRight: 10,
    justifyContent: 'center',
    alignItems: 'center',
  },
  checkboxActive: {
    backgroundColor: COLORS.primary, // Se pinta azul cuando está activo
  },
  rememberMeText: {
    fontSize: 16,
    color: COLORS.primary, // Texto Recordarme en azul
    fontWeight: '600',
  },
  actionContainer: {
    width: '100%',
    alignItems: 'center',
    position: 'absolute',
    bottom: 50, // Lo mantiene cerca de la parte inferior
  },
  loginButton: {
    width: '100%',
    height: 60,
    borderRadius: 30,
    justifyContent: 'center',
    alignItems: 'center',
    marginVertical: 15,
  },
  // Lógica visual del botón
  loginButtonDisabled: {
    backgroundColor: COLORS.disabled, // #4A4A4A Gris oscuro
  },
  loginButtonEnabled: {
    backgroundColor: COLORS.primary, // #1E3A5F Azul
  },
  loginButtonText: {
    color: '#FAF7F2', // Botones sobre fondo oscuro
    fontSize: 26,
    fontWeight: 'bold',
    letterSpacing: 1,
  },
  linkTextBase: {
    fontSize: 16,
    color: COLORS.primary, // Texto normal en azul
    fontWeight: '500',
  },
  linkTextRed: {
    color: COLORS.error, // Rojo #C44545 para los enlaces de navegación
    fontWeight: 'bold',
  },
});

export default LoginScreen;