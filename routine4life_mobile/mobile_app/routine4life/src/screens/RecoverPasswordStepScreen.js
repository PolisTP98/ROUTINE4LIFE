// src/screens/RecoverPasswordStep1Screen.js
import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, KeyboardAvoidingView, Platform, ScrollView } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';

const RecoverPasswordStep1Screen = ({ navigation }) => {
  const [email, setEmail] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [countryCode, setCountryCode] = useState('MEX +52'); // Valor por defecto

  // Lógica de interfaz: el botón se habilita si hay texto en Email O en Teléfono
  const isButtonEnabled = email.trim().length > 0 || phoneNumber.trim().length > 0;

  const handleSendMessage = () => {
    if (isButtonEnabled) {
      // Simulamos envío y navegamos al paso 2
      alert('Se ha enviado un mensaje de recuperación (Simulación)');
      navigation.navigate('RecoverPasswordStep2');
    }
  };

  const handleNotImplemented = () => {
    alert('Función aún no implementada');
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
    >
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        {/* Título Principal */}
        <View style={styles.headerContainer}>
          <Text style={styles.title}>Restablecer</Text>
          <Text style={styles.title}>contraseña</Text>
        </View>

        {/* Formulario */}
        <View style={styles.formContainer}>
          {/* Campo Correo Electrónico */}
          <TextInput
            style={styles.input}
            placeholder="Correo electrónico"
            placeholderTextColor={COLORS.inputText + '70'}
            value={email}
            onChangeText={(text) => {
              setEmail(text);
              if (text.length > 0) setPhoneNumber(''); // Limpia el otro campo si este tiene texto
            }}
            keyboardType="email-address"
            autoCapitalize="none"
          />

          {/* Separador "o" con líneas */}
          <View style={styles.separatorContainer}>
            <View style={styles.separatorLine} />
            <Text style={styles.separatorText}>o</Text>
            <View style={styles.separatorLine} />
          </View>

          {/* Etiqueta Número de teléfono */}
          <Text style={styles.label}>Número de teléfono</Text>

          {/* Selector de País y Teléfono */}
          <View style={styles.phoneInputContainer}>
            {/* Selector de país (Simulado como Touchable) */}
            <TouchableOpacity style={styles.countryPicker} onPress={handleNotImplemented}>
              <Text style={styles.countryPickerText}>{countryCode}</Text>
              <Ionicons name="caret-down" size={16} color={COLORS.primary} />
            </TouchableOpacity>

            {/* Línea divisoria vertical */}
            <View style={styles.verticalDivider} />

            {/* Input de Teléfono */}
            <TextInput
              style={styles.phoneInput}
              placeholder="XXX XXX XXXX"
              placeholderTextColor={COLORS.inputText + '70'}
              value={phoneNumber}
              onChangeText={(text) => {
                setPhoneNumber(text);
                if (text.length > 0) setEmail(''); // Limpia el otro campo si este tiene texto
              }}
              keyboardType="phone-pad"
            />
          </View>

          {/* Mensaje de ayuda (Punto) */}
          <View style={styles.helpTextContainer}>
            <Text style={styles.helpTextPoint}>•</Text>
            <Text style={styles.helpText}>
              Te enviaremos un correo electrónico o mensaje SMS con un enlace para restablecer tu contraseña
            </Text>
          </View>
        </View>

        {/* Acción y Enlace inferior */}
        <View style={styles.actionContainer}>
          {/* Botón "Enviar mensaje" con lógica dinámica */}
          <TouchableOpacity
            style={[
              styles.actionButton,
              isButtonEnabled ? styles.actionButtonEnabled : styles.actionButtonDisabled
            ]}
            onPress={handleSendMessage}
            disabled={!isButtonEnabled}
          >
            <Text style={styles.actionButtonText}>Enviar mensaje</Text>
          </TouchableOpacity>

          {/* Enlace ¿Ya tienes una cuenta? */}
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
  container: {
    flex: 1,
    backgroundColor: COLORS.background, // #F5F0E8
  },
  scrollContainer: {
    flexGrow: 1,
    paddingHorizontal: 30,
    paddingTop: '30%',
    alignItems: 'center',
  },
  headerContainer: {
    marginBottom: 60,
  },
  title: {
    fontSize: 55, // Título muy grande como en la imagen 1
    fontWeight: 'bold',
    color: COLORS.primary, // #1E3A5F
    textAlign: 'center',
    lineHeight: 60, // Ajuste para que se vea más junto el texto
  },
  formContainer: {
    width: '100%',
    marginBottom: 100, // Espacio antes del botón de acción
  },
  input: {
    backgroundColor: COLORS.inputBackground, // #D4D4D4
    color: COLORS.inputText, // #4A4A4A
    height: 55,
    borderRadius: 30,
    paddingHorizontal: 25,
    fontSize: 18,
  },
  separatorContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginVertical: 20,
  },
  separatorLine: {
    flex: 1,
    height: 2,
    backgroundColor: COLORS.primary, // Línea azul de la paleta
  },
  separatorText: {
    fontSize: 18,
    color: COLORS.primary,
    fontWeight: 'bold',
    marginHorizontal: 15,
  },
  label: {
    fontSize: 18,
    color: COLORS.primary, // Texto Número de teléfono en azul
    fontWeight: '600',
    marginBottom: 10,
    paddingLeft: 20, // Alineado visualmente
  },
  phoneInputContainer: {
    flexDirection: 'row',
    backgroundColor: COLORS.inputBackground,
    height: 55,
    borderRadius: 30,
    alignItems: 'center',
    paddingHorizontal: 5, // Un poco menos de padding para los elementos internos
  },
  countryPicker: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 15,
    width: 120, // Ancho fijo para el selector
  },
  countryPickerText: {
    fontSize: 18,
    color: COLORS.inputText,
    fontWeight: '500',
    marginRight: 5,
  },
  verticalDivider: {
    width: 2,
    height: '70%',
    backgroundColor: COLORS.primary, // Divisor vertical azul
  },
  phoneInput: {
    flex: 1,
    color: COLORS.inputText,
    fontSize: 18,
    paddingHorizontal: 15,
  },
  helpTextContainer: {
    flexDirection: 'row',
    marginTop: 15,
    paddingHorizontal: 20,
  },
  helpTextPoint: {
    fontSize: 20,
    color: COLORS.primary,
    marginRight: 10,
    lineHeight: 22,
  },
  helpText: {
    fontSize: 16,
    color: COLORS.primary, // Texto de ayuda en azul
    fontWeight: '500',
    flex: 1,
  },
  actionContainer: {
    width: '100%',
    alignItems: 'center',
    marginBottom: 50,
  },
  actionButton: {
    width: '100%',
    height: 60,
    borderRadius: 30,
    justifyContent: 'center',
    alignItems: 'center',
    marginVertical: 15,
  },
  actionButtonDisabled: {
    backgroundColor: COLORS.disabled, // #4A4A4A
  },
  actionButtonEnabled: {
    backgroundColor: COLORS.primary, // #1E3A5F
  },
  actionButtonText: {
    color: COLORS.buttonLight, // #FAF7F2
    fontSize: 26,
    fontWeight: 'bold',
  },
  linkTextBase: {
    fontSize: 16,
    color: COLORS.primary,
    fontWeight: '500',
  },
  linkTextRed: {
    color: COLORS.error, // #C44545
    fontWeight: 'bold',
  },
});

export default RecoverPasswordStep1Screen;