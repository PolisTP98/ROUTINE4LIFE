import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, KeyboardAvoidingView, Platform, ScrollView, useWindowDimensions, Alert } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';

const RecoverPasswordStep1Screen = ({ navigation }) => {
  const { width } = useWindowDimensions();
  const esPantallaGrande = width > 768;

  const [email, setEmail] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [countryCode, setCountryCode] = useState('MEX +52');

  const handleSendMessage = () => {
    // Tomamos el correo, si no hay tomamos el teléfono, y si ambos están vacíos mandamos un texto por defecto
    const datoIngresado = email.trim() || phoneNumber.trim() || 'correo_simulado@test.com';

    // Lanzamos el mensaje de éxito (Simulación)
    Alert.alert(
      'Mensaje enviado', 
      `Se simuló el envío del enlace de recuperación a: ${datoIngresado}`
    );

    // Redireccionamos INMEDIATAMENTE a la Step 2, sin esperar a que el usuario cierre la alerta
    navigation.navigate('RecoverPasswordStep2', { email: datoIngresado });
  };

  const handleNotImplemented = () => {
    Alert.alert('Aviso', 'Función de cambio de país aún no implementada');
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
    >
      <ScrollView 
        contentContainerStyle={[
          styles.scrollContainer, 
          esPantallaGrande ? styles.scrollContainerWeb : null
        ]}
      >
        <View style={styles.headerContainer}>
          <Text style={styles.title}>Restablecer</Text>
          <Text style={styles.title}>contraseña</Text>
        </View>

        <View style={styles.formContainer}>
          <TextInput
            style={styles.input}
            placeholder="Correo electrónico"
            placeholderTextColor={COLORS.inputText + '70'}
            value={email}
            onChangeText={(text) => {
              setEmail(text);
              if (text.length > 0) setPhoneNumber('');
            }}
            keyboardType="email-address"
            autoCapitalize="none"
          />

          <View style={styles.separatorContainer}>
            <View style={styles.separatorLine} />
            <Text style={styles.separatorText}>o</Text>
            <View style={styles.separatorLine} />
          </View>

          <Text style={styles.label}>Número de teléfono</Text>

          <View style={styles.phoneInputContainer}>
            <TouchableOpacity style={styles.countryPicker} onPress={handleNotImplemented}>
              <Text style={styles.countryPickerText}>{countryCode}</Text>
              <Ionicons name="caret-down" size={16} color={COLORS.primary} />
            </TouchableOpacity>

            <View style={styles.verticalDivider} />

            <TextInput
              style={styles.phoneInput}
              placeholder="XXX XXX XXXX"
              placeholderTextColor={COLORS.inputText + '70'}
              value={phoneNumber}
              onChangeText={(text) => {
                setPhoneNumber(text);
                if (text.length > 0) setEmail('');
              }}
              keyboardType="phone-pad"
            />
          </View>

          <View style={styles.helpTextContainer}>
            <Text style={styles.helpTextPoint}>•</Text>
            <Text style={styles.helpText}>
              Te enviaremos un correo electrónico o mensaje SMS con un enlace para restablecer tu contraseña
            </Text>
          </View>
        </View>

        <View style={styles.actionContainer}>
          {/* El botón ahora siempre está habilitado */}
          <TouchableOpacity
            style={[styles.actionButton, styles.actionButtonEnabled]}
            onPress={handleSendMessage}
          >
            <Text style={styles.actionButtonText}>Enviar mensaje</Text>
          </TouchableOpacity>

          <Text style={styles.linkTextBase}>
            ¿Ya tienes una cuenta?{' '}
            <Text style={styles.linkTextRed} onPress={() => navigation.navigate('Login')}>
              Iniciar sesión
            </Text>
          </Text>
        </View>
      </ScrollView>
    </KeyboardAvoidingView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: COLORS.background },
  scrollContainer: { flexGrow: 1, paddingHorizontal: 30, paddingTop: '30%', alignItems: 'center' },
  scrollContainerWeb: { alignSelf: 'center', width: '100%', maxWidth: 500, paddingTop: '10%' },
  headerContainer: { marginBottom: 60 },
  title: { fontSize: 55, fontWeight: 'bold', color: COLORS.primary, textAlign: 'center', lineHeight: 60 },
  formContainer: { width: '100%', marginBottom: 100 },
  input: { backgroundColor: COLORS.inputBackground, color: COLORS.inputText, height: 55, borderRadius: 30, paddingHorizontal: 25, fontSize: 18 },
  separatorContainer: { flexDirection: 'row', alignItems: 'center', marginVertical: 20 },
  separatorLine: { flex: 1, height: 2, backgroundColor: COLORS.primary },
  separatorText: { fontSize: 18, color: COLORS.primary, fontWeight: 'bold', marginHorizontal: 15 },
  label: { fontSize: 18, color: COLORS.primary, fontWeight: '600', marginBottom: 10, paddingLeft: 20 },
  phoneInputContainer: { flexDirection: 'row', backgroundColor: COLORS.inputBackground, height: 55, borderRadius: 30, alignItems: 'center', paddingHorizontal: 5 },
  countryPicker: { flexDirection: 'row', alignItems: 'center', justifyContent: 'center', paddingHorizontal: 15, width: 120 },
  countryPickerText: { fontSize: 18, color: COLORS.inputText, fontWeight: '500', marginRight: 5 },
  verticalDivider: { width: 2, height: '70%', backgroundColor: COLORS.primary },
  phoneInput: { flex: 1, color: COLORS.inputText, fontSize: 18, paddingHorizontal: 15 },
  helpTextContainer: { flexDirection: 'row', marginTop: 15, paddingHorizontal: 20 },
  helpTextPoint: { fontSize: 20, color: COLORS.primary, marginRight: 10, lineHeight: 22 },
  helpText: { fontSize: 16, color: COLORS.primary, fontWeight: '500', flex: 1 },
  actionContainer: { width: '100%', alignItems: 'center', marginBottom: 50 },
  actionButton: { width: '100%', height: 60, borderRadius: 30, justifyContent: 'center', alignItems: 'center', marginVertical: 15 },
  actionButtonEnabled: { backgroundColor: COLORS.primary },
  actionButtonText: { color: COLORS.buttonLight, fontSize: 26, fontWeight: 'bold' },
  linkTextBase: { fontSize: 16, color: COLORS.primary, fontWeight: '500' },
  linkTextRed: { color: COLORS.error, fontWeight: 'bold' },
});

export default RecoverPasswordStep1Screen;