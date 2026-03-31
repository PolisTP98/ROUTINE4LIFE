import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, KeyboardAvoidingView, Platform, ScrollView } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';
import SuccessToast from '../components/SuccessToast';

const LoginScreen = ({ navigation, route }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [secureTextEntry, setSecureTextEntry] = useState(true);
  
  // Estados para el Toast
  const [showToast, setShowToast] = useState(false);
  const [toastMessage, setToastMessage] = useState('');

  useEffect(() => {
    // Caso 1: Registro Exitoso
    if (route.params?.registered) {
      setToastMessage("Has completado el registro de tu cuenta exitosamente");
      setShowToast(true);
      navigation.setParams({ registered: undefined });
    }
    // Caso 2: Restablecimiento Exitoso
    else if (route.params?.recovered) {
      setToastMessage("Tu contraseña fue reestablecida exitosamente");
      setShowToast(true);
      navigation.setParams({ recovered: undefined });
    }
  }, [route.params]);

  const isButtonEnabled = email.trim().length > 0 && password.trim().length > 0;

  return (
    <View style={{ flex: 1 }}>
      <SuccessToast 
        visible={showToast} 
        message={toastMessage} 
        onHide={() => setShowToast(false)} 
      />

      <KeyboardAvoidingView style={styles.container} behavior={Platform.OS === 'ios' ? 'padding' : 'height'}>
        <ScrollView contentContainerStyle={styles.scrollContainer}>
          <Text style={styles.title}>Iniciar sesión</Text>
          <View style={styles.formContainer}>
            <TextInput
              style={styles.input}
              placeholder="Correo electrónico"
              placeholderTextColor={COLORS.inputText + '70'}
              value={email}
              onChangeText={setEmail}
              autoCapitalize="none"
            />
            <View style={styles.passwordInputContainer}>
              <TextInput
                style={styles.passwordInput}
                placeholder="Contraseña"
                placeholderTextColor={COLORS.inputText + '70'}
                value={password}
                onChangeText={setPassword}
                secureTextEntry={secureTextEntry}
              />
              <TouchableOpacity onPress={() => setSecureTextEntry(!secureTextEntry)}>
                <Ionicons name={secureTextEntry ? 'eye-outline' : 'eye-off-outline'} size={28} color={COLORS.primary} />
              </TouchableOpacity>
            </View>
            <View style={styles.rememberRow}>
                <View style={styles.checkbox} />
                <Text style={styles.rememberText}>Recordarme</Text>
            </View>
          </View>

          <View style={styles.actionContainer}>
            <Text style={styles.linkTextBase}>
              ¿Olvidaste tu contraseña?{' '}
              <Text style={styles.linkTextRed} onPress={() => navigation.navigate('RecoverPasswordStep1')}>Reestablecer</Text>
            </Text>
            <TouchableOpacity
              style={[styles.loginButton, isButtonEnabled ? styles.loginButtonEnabled : styles.loginButtonDisabled]}
              onPress={() => navigation.navigate('Home')}
              disabled={!isButtonEnabled}
            >
              <Text style={styles.loginButtonText}>Iniciar sesión</Text>
            </TouchableOpacity>
            <Text style={styles.linkTextBase}>
              ¿No tienes una cuenta?{' '}
              <Text style={styles.linkTextRed} onPress={() => navigation.navigate('Register')}>Registrarse</Text>
            </Text>
          </View>
        </ScrollView>
      </KeyboardAvoidingView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: COLORS.background },
  scrollContainer: { flexGrow: 1, paddingHorizontal: 35, paddingTop: '35%', alignItems: 'center' },
  title: { fontSize: 55, fontWeight: 'bold', color: COLORS.primary, textAlign: 'center', marginBottom: 60 },
  formContainer: { width: '100%', marginBottom: 40 },
  input: { backgroundColor: COLORS.inputBackground, height: 55, borderRadius: 30, paddingHorizontal: 25, fontSize: 18, marginBottom: 15, color: COLORS.inputText },
  passwordInputContainer: { flexDirection: 'row', backgroundColor: COLORS.inputBackground, height: 55, borderRadius: 30, alignItems: 'center', paddingHorizontal: 20, marginBottom: 15 },
  passwordInput: { flex: 1, color: COLORS.inputText, fontSize: 18 },
  rememberRow: { flexDirection: 'row', alignItems: 'center', marginLeft: 10 },
  checkbox: { width: 22, height: 22, borderRadius: 11, backgroundColor: '#D4D4D4', marginRight: 10 },
  rememberText: { fontSize: 16, color: COLORS.primary, fontWeight: '600' },
  actionContainer: { width: '100%', alignItems: 'center' },
  loginButton: { width: '100%', height: 60, borderRadius: 30, justifyContent: 'center', alignItems: 'center', marginVertical: 15 },
  loginButtonDisabled: { backgroundColor: COLORS.disabled },
  loginButtonEnabled: { backgroundColor: COLORS.primary },
  loginButtonText: { color: COLORS.buttonLight, fontSize: 26, fontWeight: 'bold' },
  linkTextBase: { fontSize: 16, color: COLORS.primary, fontWeight: '500' },
  linkTextRed: { color: COLORS.error, fontWeight: 'bold' },
});

export default LoginScreen;