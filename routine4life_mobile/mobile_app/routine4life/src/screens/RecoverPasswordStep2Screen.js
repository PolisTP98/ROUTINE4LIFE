import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, KeyboardAvoidingView, Platform, ScrollView } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';

const RecoverPasswordStep2Screen = ({ navigation }) => {
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [secureTextEntry1, setSecureTextEntry1] = useState(true);
  const [secureTextEntry2, setSecureTextEntry2] = useState(true);

  const reqLength = password.length >= 8;
  const reqUpper = /[A-Z]/.test(password);
  const reqSpecial = /[0-9!@#$/()={}=.,;:_]/.test(password);
  const reqNoSeq = password.length > 0 && !/(.)\1{2}/.test(password);
  const doMatch = password.length > 0 && password === confirmPassword;

  const isButtonEnabled = reqLength && reqUpper && reqSpecial && reqNoSeq && doMatch;

  const handleReset = () => {
    if (isButtonEnabled) {
      // CORRECCIÓN: Redirigimos al Login pasando el parámetro de éxito para que salte el Toast
      navigation.navigate('Login', { recovered: true });
    }
  };

  const RequirementItem = ({ text, isMet }) => {
    const iconName = isMet ? "checkmark" : "close";
    const statusColor = isMet ? COLORS.success : COLORS.error;
    return (
      <View style={styles.reqRow}>
        <Ionicons name={iconName} size={16} color={statusColor} style={styles.reqIcon} />
        <Text style={[styles.reqText, { color: statusColor }]}>{text}</Text>
      </View>
    );
  };

  return (
    <KeyboardAvoidingView style={styles.container} behavior={Platform.OS === 'ios' ? 'padding' : 'height'}>
      <ScrollView contentContainerStyle={styles.scroll} showsVerticalScrollIndicator={false}>
        <Text style={styles.title}>Restablecer{'\n'}contraseña</Text>

        <View style={styles.form}>
          <View style={styles.inputWrapper}>
            <TextInput
              style={styles.input}
              placeholder="Nueva contraseña"
              placeholderTextColor={COLORS.inputText + '80'}
              value={password}
              onChangeText={setPassword}
              secureTextEntry={secureTextEntry1}
            />
            <TouchableOpacity onPress={() => setSecureTextEntry1(!secureTextEntry1)}>
              <Ionicons name={secureTextEntry1 ? "eye-off" : "eye"} size={24} color={COLORS.primary} />
            </TouchableOpacity>
          </View>

          <View style={styles.reqList}>
            <RequirementItem text="La contraseña debe tener mínimo 8 caracteres" isMet={reqLength} />
            <RequirementItem text="La contraseña debe incluir letras en mayúscula" isMet={reqUpper} />
            <RequirementItem text="La contraseña debe incluir números y caracteres especiales: *?!@#$/()={}=.,;:_" isMet={reqSpecial} />
            <RequirementItem text="La contraseña no debe tener más de dos caracteres repetidos o números en secuencia" isMet={reqNoSeq} />
          </View>

          <View style={styles.inputWrapper}>
            <TextInput
              style={styles.input}
              placeholder="Confirmar contraseña"
              placeholderTextColor={COLORS.inputText + '80'}
              value={confirmPassword}
              onChangeText={setConfirmPassword}
              secureTextEntry={secureTextEntry2}
            />
            <TouchableOpacity onPress={() => setSecureTextEntry2(!secureTextEntry2)}>
              <Ionicons name={secureTextEntry2 ? "eye-off" : "eye"} size={24} color={COLORS.primary} />
            </TouchableOpacity>
          </View>

          <View style={styles.reqList}>
            <RequirementItem text="Las contraseñas coinciden" isMet={doMatch} />
          </View>
        </View>

        <View style={styles.footer}>
          <TouchableOpacity
            style={[styles.btn, isButtonEnabled ? styles.btnActive : styles.btnDisabled]}
            disabled={!isButtonEnabled}
            onPress={handleReset}
          >
            <Text style={styles.btnText}>Restablecer</Text>
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
  scroll: { flexGrow: 1, padding: 30, alignItems: 'center', paddingTop: '20%' },
  title: { fontSize: 48, fontWeight: 'bold', color: COLORS.primary, textAlign: 'center', marginBottom: 50 },
  form: { width: '100%' },
  inputWrapper: { flexDirection: 'row', backgroundColor: COLORS.inputBackground, borderRadius: 25, height: 55, alignItems: 'center', paddingHorizontal: 20, marginBottom: 10 },
  input: { flex: 1, color: COLORS.inputText, fontSize: 18 },
  reqList: { paddingHorizontal: 20, marginBottom: 20 },
  reqRow: { flexDirection: 'row', alignItems: 'flex-start', marginBottom: 6 },
  reqIcon: { marginTop: 2, marginRight: 8 },
  reqText: { fontSize: 14, flex: 1, fontWeight: '500' },
  footer: { width: '100%', alignItems: 'center', marginTop: 20 },
  btn: { width: '100%', height: 60, borderRadius: 30, justifyContent: 'center', alignItems: 'center', marginBottom: 20 },
  btnDisabled: { backgroundColor: COLORS.disabled },
  btnActive: { backgroundColor: COLORS.primary },
  btnText: { color: COLORS.buttonLight, fontSize: 22, fontWeight: 'bold' },
  loginLink: { color: COLORS.primary, fontSize: 16 },
  linkRed: { color: COLORS.error, fontWeight: 'bold' }
});

export default RecoverPasswordStep2Screen;