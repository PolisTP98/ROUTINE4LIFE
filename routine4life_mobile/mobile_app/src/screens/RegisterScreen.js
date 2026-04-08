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
  Modal,
  FlatList,
  ActivityIndicator
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';
import { API_URL } from '../api/config'; 

const RegisterScreen = ({ navigation }) => {
  const [formData, setFormData] = useState({
    fullName: '',
    birthDate: '',
    gender: '', 
    id_sexo: null, 
    email: '',
    phone: ''
  });

  const [genders, setGenders] = useState([]);
  const [showGenderModal, setShowGenderModal] = useState(false);
  const [isLoadingGenders, setIsLoadingGenders] = useState(false);

  useEffect(() => {
    const fetchGenders = async () => {
      setIsLoadingGenders(true);
      try {
        const response = await fetch(`${API_URL}/auth-movil/sexos`);
        if (response.ok) {
          const data = await response.json();
          setGenders(data);
        }
      } catch (error) {
        console.error("Error al obtener los sexos:", error);
      } finally {
        setIsLoadingGenders(false);
      }
    };

    fetchGenders();
  }, []);

  const isButtonEnabled = 
    formData.fullName.trim().length > 0 &&
    formData.birthDate.trim().length > 0 &&
    formData.id_sexo !== null &&
    formData.email.trim().length > 0 &&
    formData.phone.trim().length > 0;

  const updateField = (field, value) => {
    setFormData({ ...formData, [field]: value });
  };

  const handleNotImplemented = (msg) => alert(`${msg} aún no implementado`);

  return (
    <SafeAreaView style={styles.container}>
      <KeyboardAvoidingView 
        style={{ flex: 1 }} 
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      >
        <ScrollView 
          contentContainerStyle={styles.scroll} 
          showsVerticalScrollIndicator={false}
          keyboardShouldPersistTaps="handled"
        >
          <Text style={styles.title}>Registrarse</Text>

          <View style={styles.form}>
            <TextInput
              style={styles.input}
              placeholder="Nombre completo"
              placeholderTextColor={COLORS.inputText + '80'}
              onChangeText={(v) => updateField('fullName', v)}
            />

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

            {/* Selector de Sexo */}
            <TouchableOpacity 
              style={styles.inputWithIcon} 
              onPress={() => setShowGenderModal(true)}
              activeOpacity={0.7}
            >
              <Text style={[styles.flexInput, { color: formData.gender ? COLORS.inputText : COLORS.inputText + '80' }]}>
                {formData.gender || "Sexo"}
              </Text>
              <Ionicons name="caret-down" size={24} color={COLORS.primary} />
            </TouchableOpacity>

            <TextInput
              style={[styles.input, { marginTop: 10 }]}
              placeholder="Correo electrónico"
              placeholderTextColor={COLORS.inputText + '80'}
              keyboardType="email-address"
              autoCapitalize="none"
              onChangeText={(v) => updateField('email', v)}
            />

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
              onPress={() => navigation.navigate('RegisterPassword', { formData })} 
              activeOpacity={0.8}
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

      {/* Modal para Seleccionar Sexo */}
      <Modal
        visible={showGenderModal}
        transparent={true}
        animationType="fade"
        onRequestClose={() => setShowGenderModal(false)}
      >
        <TouchableOpacity 
          style={styles.modalOverlay} 
          activeOpacity={1} 
          onPress={() => setShowGenderModal(false)}
        >
          <View style={styles.modalContent}>
            <Text style={styles.modalTitle}>Selecciona tu sexo</Text>
            
            {isLoadingGenders ? (
              <ActivityIndicator size="large" color={COLORS.primary} style={{ marginVertical: 20 }} />
            ) : (
              <FlatList
                data={genders}
                keyExtractor={(item) => item.id_sexo.toString()}
                renderItem={({ item }) => (
                  <TouchableOpacity 
                    style={styles.modalOption}
                    onPress={() => {
                      setFormData({ 
                        ...formData, 
                        gender: item.nombre, 
                        id_sexo: item.id_sexo 
                      });
                      setShowGenderModal(false);
                    }}
                  >
                    <Text style={styles.modalOptionText}>{item.nombre}</Text>
                  </TouchableOpacity>
                )}
                ListEmptyComponent={<Text style={{textAlign: 'center', marginVertical: 10}}>No hay opciones disponibles</Text>}
              />
            )}
          </View>
        </TouchableOpacity>
      </Modal>

    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: COLORS.background },
  scroll: { flexGrow: 1, padding: 35, alignItems: 'center', paddingTop: '10%' },
  title: { fontSize: 50, fontWeight: 'bold', color: COLORS.primary, marginBottom: 40 },
  form: { width: '100%' },
  label: { fontSize: 18, color: COLORS.primary, fontWeight: '600', marginLeft: 15, marginTop: 15, marginBottom: 5 },
  input: { backgroundColor: COLORS.inputBackground, height: 55, borderRadius: 30, paddingHorizontal: 25, fontSize: 18, color: COLORS.inputText, marginBottom: 10 },
  inputWithIcon: { flexDirection: 'row', backgroundColor: COLORS.inputBackground, height: 55, borderRadius: 30, paddingHorizontal: 20, alignItems: 'center', marginBottom: 10 },
  flexInput: { flex: 1, fontSize: 18, color: COLORS.inputText },
  phoneContainer: { flexDirection: 'row', backgroundColor: COLORS.inputBackground, height: 55, borderRadius: 30, alignItems: 'center', paddingHorizontal: 10 },
  countryCode: { flexDirection: 'row', alignItems: 'center', paddingHorizontal: 10 },
  countryText: { fontSize: 18, color: COLORS.inputText, marginRight: 5 },
  verticalDivider: { width: 2, height: '60%', backgroundColor: COLORS.primary },
  phoneInput: { flex: 1, paddingHorizontal: 15, fontSize: 18, color: COLORS.inputText },
  footer: { width: '100%', alignItems: 'center', marginTop: 40, marginBottom: 30 },
  btn: { width: '100%', height: 65, borderRadius: 35, flexDirection: 'row', justifyContent: 'center', alignItems: 'center', marginBottom: 20 },
  btnDisabled: { backgroundColor: COLORS.disabled },
  btnActive: { backgroundColor: COLORS.primary },
  btnText: { color: COLORS.buttonLight, fontSize: 26, fontWeight: 'bold', marginRight: 10 },
  loginLink: { color: COLORS.primary, fontSize: 16, fontWeight: '500' },
  linkRed: { color: COLORS.error, fontWeight: 'bold' },
  modalOverlay: { flex: 1, backgroundColor: 'rgba(0,0,0,0.5)', justifyContent: 'center', alignItems: 'center' },
  modalContent: { width: '80%', backgroundColor: COLORS.background, borderRadius: 20, padding: 20, maxHeight: '50%' },
  modalTitle: { fontSize: 20, fontWeight: 'bold', color: COLORS.primary, marginBottom: 15, textAlign: 'center' },
  modalOption: { paddingVertical: 15, borderBottomWidth: 1, borderBottomColor: COLORS.inputBackground },
  modalOptionText: { fontSize: 18, color: COLORS.inputText, textAlign: 'center' }
});

export default RegisterScreen;