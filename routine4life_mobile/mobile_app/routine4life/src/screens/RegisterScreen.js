// src/screens/RegisterScreen.js
import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, KeyboardAvoidingView, Platform, ScrollView } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';

const RegisterScreen = ({ navigation }) => {
  const [formData, setFormData] = useState({
    fullName: '',
    birthDate: '',
    gender: '',
    email: '',
    phone: ''
  });

  // Lógica: Todos los campos deben tener texto para habilitar
  const isButtonEnabled = Object.values(formData).every(value => value.trim().length > 0);

  const updateField = (field, value) => {
    setFormData({ ...formData, [field]: value });
  };

  const handleNotImplemented = (msg) => alert(`${msg} aún no implementado`);

  return (
    <KeyboardAvoidingView 
      style={styles.container} 
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
    >
      <ScrollView contentContainerStyle={styles.scroll}>
        <Text style={styles.title}>Registrarse</Text>

        <View style={styles.form}>
          {/* Nombre Completo */}
          <TextInput
            style={styles.input}
            placeholder="Nombre completo"
            placeholderTextColor={COLORS.inputText + '80'}
            onChangeText={(v) => updateField('fullName', v)}
          />

          {/* Fecha de Nacimiento */}
          <Text style={styles.label}>Fecha de nacimiento</Text>
          <View style={styles.inputWithIcon}>
            <TextInput
              style={styles.flexInput}
              placeholder="DD / MM / AAAA"
              placeholderTextColor={COLORS.inputText + '80'}
              onChangeText={(v) => updateField('birthDate', v)}
            />
            <Ionicons name="calendar-outline" size={32} color={COLORS.primary} />
          </View>

          {/* Sexo (Simulado como botón para abrir selector) */}
          <TouchableOpacity 
            style={styles.inputWithIcon} 
            onPress={() => {
                updateField('gender', 'Otro'); // Simulación de selección
                handleNotImplemented('Selector de Sexo');
            }}
          >
            <Text style={[styles.flexInput, { color: formData.gender ? COLORS.inputText : COLORS.inputText + '80', paddingTop: 15 }]}>
              {formData.gender || "Sexo"}
            </Text>
            <Ionicons name="caret-down" size={24} color={COLORS.primary} />
          </TouchableOpacity>

          {/* Correo */}
          <TextInput
            style={[styles.input, { marginTop: 10 }]}
            placeholder="Correo electrónico"
            placeholderTextColor={COLORS.inputText + '80'}
            keyboardType="email-address"
            onChangeText={(v) => updateField('email', v)}
          />

          {/* Teléfono */}
          <Text style={styles.label}>Número de teléfono</Text>
          <View style={styles.phoneContainer}>
            <TouchableOpacity style={styles.countryCode} onPress={() => handleNotImplemented('Países')}>
              <Text style={styles.countryText}>MEX +52</Text>
              <Ionicons name="caret-down" size={16} color={COLORS.primary} />
            </TouchableOpacity>
            <View style={styles.verticalDivider} />
            <TextInput
              style={styles.phoneInput}
              placeholder="XXX XXX XXXX"
              placeholderTextColor={COLORS.inputText + '80'}
              keyboardType="phone-pad"
              onChangeText={(v) => updateField('phone', v)}
            />
          </View>
        </View>

        <View style={styles.footer}>
          <TouchableOpacity
            style={[styles.btn, isButtonEnabled ? styles.btnActive : styles.btnDisabled]}
            disabled={!isButtonEnabled}
            onPress={() => navigation.navigate('RegisterPassword')} // <- CAMBIO AQUÍ
          >
            <Text style={styles.btnText}>Continuar</Text>
            <Ionicons name="chevron-forward" size={35} color={COLORS.buttonLight} />
          </TouchableOpacity>

          <Text style={styles.loginLink}>
            ¿Ya tienes una cuenta? <Text style={styles.linkRed} onPress={() => navigation.navigate('Login')}>Iniciar sesión</Text>
          </Text>
        </View>
      </ScrollView>
    </KeyboardAvoidingView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: COLORS.background },
  scroll: { flexGrow: 1, padding: 35, alignItems: 'center', paddingTop: '15%' },
  title: { fontSize: 52, fontWeight: 'bold', color: COLORS.primary, marginBottom: 40 },
  form: { width: '100%' },
  label: { fontSize: 18, color: COLORS.primary, fontWeight: '600', marginLeft: 15, marginTop: 15, marginBottom: 5 },
  input: {
    backgroundColor: COLORS.inputBackground,
    height: 55,
    borderRadius: 30,
    paddingHorizontal: 25,
    fontSize: 18,
    color: COLORS.inputText,
    marginBottom: 10
  },
  inputWithIcon: {
    flexDirection: 'row',
    backgroundColor: COLORS.inputBackground,
    height: 55,
    borderRadius: 30,
    paddingHorizontal: 20,
    alignItems: 'center',
    marginBottom: 10
  },
  flexInput: { flex: 1, fontSize: 18, color: COLORS.inputText },
  phoneContainer: {
    flexDirection: 'row',
    backgroundColor: COLORS.inputBackground,
    height: 55,
    borderRadius: 30,
    alignItems: 'center',
    paddingHorizontal: 10
  },
  countryCode: { flexDirection: 'row', alignItems: 'center', paddingHorizontal: 10 },
  countryText: { fontSize: 18, color: COLORS.inputText, marginRight: 5 },
  verticalDivider: { width: 2, height: '60%', backgroundColor: COLORS.primary },
  phoneInput: { flex: 1, paddingHorizontal: 15, fontSize: 18, color: COLORS.inputText },
  footer: { width: '100%', alignItems: 'center', marginTop: 40 },
  btn: { 
    width: '100%', 
    height: 65, 
    borderRadius: 35, 
    flexDirection: 'row', 
    justifyContent: 'center', 
    alignItems: 'center', 
    marginBottom: 20 
  },
  btnDisabled: { backgroundColor: COLORS.disabled },
  btnActive: { backgroundColor: COLORS.primary },
  btnText: { color: COLORS.buttonLight, fontSize: 28, fontWeight: 'bold', marginRight: 10 },
  loginLink: { color: COLORS.primary, fontSize: 16 },
  linkRed: { color: COLORS.error, fontWeight: 'bold' }
});

export default RegisterScreen;