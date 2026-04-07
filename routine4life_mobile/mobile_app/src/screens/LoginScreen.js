import React, { useState, useEffect } from 'react';
import { 
  View, 
  Text, 
  TextInput, 
  TouchableOpacity, 
  StyleSheet, 
  KeyboardAvoidingView, 
  Platform, 
  ScrollView,
  ActivityIndicator
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context'; 
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';
import SuccessToast from '../components/SuccessToast';
import { API_URL } from '../api/config';

const LoginScreen = ({ navigation, route }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [secureTextEntry, setSecureTextEntry] = useState(true);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  
  const [showToast, setShowToast] = useState(false);
  const [toastMessage, setToastMessage] = useState('');

  useEffect(() => {
    if (route.params?.registered) {
      setToastMessage("Has completado el registro de tu cuenta exitosamente");
      setShowToast(true);
      navigation.setParams({ registered: undefined });
    }
    else if (route.params?.recovered) {
      setToastMessage("Tu contraseña fue reestablecida exitosamente");
      setShowToast(true);
      navigation.setParams({ recovered: undefined });
    }
  }, [route.params]);

  const isButtonEnabled = email.trim().length > 0 && password.trim().length > 0;

  const handleLogin = async () => {
    setErrorMessage('');
    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.trim())) {
      setErrorMessage('Por favor, ingresa un correo electrónico válido.');
      return;
    }

    setIsLoading(true);
    try {
      const response = await fetch(`${API_URL}/auth-movil/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email.trim(),
          contrasena: password,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        navigation.replace('Main', { id_paciente: data.id_paciente }); 
      } else {
        const errorMsg = typeof data.detail === 'string' ? data.detail : 'Correo o contraseña incorrectos.';
        setErrorMessage(errorMsg);
      }
    } catch (error) {
      setErrorMessage('Error de conexión. Verifica tu red o el servidor.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <SuccessToast 
        visible={showToast} 
        message={toastMessage} 
        onHide={() => setShowToast(false)} 
      />

      <KeyboardAvoidingView 
        style={{ flex: 1 }} 
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      >
        <ScrollView 
          contentContainerStyle={styles.scrollContainer} 
          showsVerticalScrollIndicator={false}
          keyboardShouldPersistTaps="handled"
        >
          <Text style={styles.title}>Iniciar sesión</Text>
          
          <View style={styles.formContainer}>
            <TextInput
              style={styles.input}
              placeholder="Correo electrónico"
              placeholderTextColor={COLORS.inputText + '70'}
              value={email}
              onChangeText={(text) => {
                setEmail(text);
                setErrorMessage('');
              }}
              autoCapitalize="none"
              keyboardType="email-address"
            />
            
            <View style={styles.passwordInputContainer}>
              <TextInput
                style={styles.passwordInput}
                placeholder="Contraseña"
                placeholderTextColor={COLORS.inputText + '70'}
                value={password}
                onChangeText={(text) => {
                  setPassword(text);
                  setErrorMessage('');
                }}
                secureTextEntry={secureTextEntry}
              />
              <TouchableOpacity onPress={() => setSecureTextEntry(!secureTextEntry)}>
                <Ionicons 
                  name={secureTextEntry ? 'eye-outline' : 'eye-off-outline'} 
                  size={24} 
                  color={COLORS.primary} 
                />
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
              <Text 
                style={styles.linkTextRed} 
                onPress={() => navigation.navigate('RecoverPasswordStep1')}
              >
                Reestablecer
              </Text>
            </Text>

            {errorMessage !== '' && (
              <Text style={styles.errorText}>{errorMessage}</Text>
            )}

            <TouchableOpacity
              style={[
                styles.loginButton, 
                isButtonEnabled && !isLoading ? styles.loginButtonEnabled : styles.loginButtonDisabled
              ]}
              onPress={handleLogin}
              disabled={!isButtonEnabled || isLoading}
              activeOpacity={0.8}
            >
              {isLoading ? (
                <ActivityIndicator color={COLORS.buttonLight} size="large" />
              ) : (
                <Text style={styles.loginButtonText}>Iniciar sesión</Text>
              )}
            </TouchableOpacity>

            <Text style={styles.linkTextBase}>
              ¿No tienes una cuenta?{' '}
              <Text 
                style={styles.linkTextRed} 
                onPress={() => navigation.navigate('Register')}
              >
                Registrarse
              </Text>
            </Text>
          </View>
        </ScrollView>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: COLORS.background },
  scrollContainer: { 
    flexGrow: 1, 
    paddingHorizontal: 35, 
    paddingTop: '20%', 
    alignItems: 'center' 
  },
  title: { 
    fontSize: 48, 
    fontWeight: 'bold', 
    color: COLORS.primary, 
    textAlign: 'center', 
    marginBottom: 50 
  },
  formContainer: { width: '100%', marginBottom: 30 },
  input: { 
    backgroundColor: COLORS.inputBackground, 
    height: 55, 
    borderRadius: 30, 
    paddingHorizontal: 25, 
    fontSize: 18, 
    marginBottom: 15, 
    color: COLORS.inputText 
  },
  passwordInputContainer: { 
    flexDirection: 'row', 
    backgroundColor: COLORS.inputBackground, 
    height: 55, 
    borderRadius: 30, 
    alignItems: 'center', 
    paddingHorizontal: 20, 
    marginBottom: 15 
  },
  passwordInput: { flex: 1, color: COLORS.inputText, fontSize: 18 },
  rememberRow: { flexDirection: 'row', alignItems: 'center', marginLeft: 10 },
  checkbox: { 
    width: 22, 
    height: 22, 
    borderRadius: 11, 
    backgroundColor: '#D4D4D4', 
    marginRight: 10 
  },
  rememberText: { fontSize: 16, color: COLORS.primary, fontWeight: '600' },
  actionContainer: { width: '100%', alignItems: 'center' },
  errorText: {
    color: COLORS.error,
    fontSize: 14,
    fontWeight: '500',
    marginTop: 15,
    textAlign: 'center',
    paddingHorizontal: 10,
  },
  loginButton: { 
    width: '100%', 
    height: 60, 
    borderRadius: 30, 
    justifyContent: 'center', 
    alignItems: 'center', 
    marginVertical: 15 
  },
  loginButtonDisabled: { backgroundColor: COLORS.disabled },
  loginButtonEnabled: { backgroundColor: COLORS.primary },
  loginButtonText: { color: COLORS.buttonLight, fontSize: 24, fontWeight: 'bold' },
  linkTextBase: { fontSize: 16, color: COLORS.primary, fontWeight: '500' },
  linkTextRed: { color: COLORS.error, fontWeight: 'bold' },
});

export default LoginScreen;