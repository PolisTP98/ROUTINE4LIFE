import React, { useState, useEffect } from 'react';
import { 
  View, 
  Text, 
  TextInput, 
  TouchableOpacity, 
  StyleSheet, 
  KeyboardAvoidingView, 
  Platform, 
  ScrollView 
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context'; // Importante para SDK 54
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';
import SuccessToast from '../components/SuccessToast';

const LoginScreen = ({ navigation, route }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [secureTextEntry, setSecureTextEntry] = useState(true);
  
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

  return (
    // SafeAreaView asegura que el contenido no choque con la barra de estado
    <SafeAreaView style={styles.container}>
      <SuccessToast 
        visible={showToast} 
        message={toastMessage} 
        onHide={() => setShowToast(false)} 
      />

      <KeyboardAvoidingView 
        style={{ flex: 1 }} 
        behavior={Platform.OS === 'ios' ? 'padding' : undefined} // En Android suele ser mejor dejarlo undefined o usar 'height'
      >
        <ScrollView 
          contentContainerStyle={styles.scrollContainer} 
          showsVerticalScrollIndicator={false}
          keyboardShouldPersistTaps="handled" // Permite tocar botones mientras el teclado está abierto
        >
          <Text style={styles.title}>Iniciar sesión</Text>
          
          <View style={styles.formContainer}>
            <TextInput
              style={styles.input}
              placeholder="Correo electrónico"
              placeholderTextColor={COLORS.inputText + '70'}
              value={email}
              onChangeText={setEmail}
              autoCapitalize="none"
              keyboardType="email-address"
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
                <Ionicons 
                  name={secureTextEntry ? 'eye-outline' : 'eye-off-outline'} 
                  size={24} // Un poco más pequeño para mejor balance visual
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

            <TouchableOpacity
              style={[
                styles.loginButton, 
                isButtonEnabled ? styles.loginButtonEnabled : styles.loginButtonDisabled
              ]}
              onPress={() => navigation.replace('AppDrawer')}
              disabled={!isButtonEnabled}
              activeOpacity={0.8}
            >
              <Text style={styles.loginButtonText}>Iniciar sesión</Text>
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
    paddingTop: '20%', // Reducido un poco para dar aire en pantallas pequeñas
    alignItems: 'center' 
  },
  title: { 
    fontSize: 48, // Ajustado de 55 para evitar desbordamientos en pantallas medianas
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