import React, { useState } from 'react';
import { 
  View, 
  Text, 
  StyleSheet, 
  Modal, 
  TouchableOpacity, 
  TextInput, 
  KeyboardAvoidingView, 
  Platform,
  Pressable
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';

const FilterModal = ({ visible, onClose, onFilter }) => {
  const [desde, setDesde] = useState('');
  const [hasta, setHasta] = useState('');

  const isButtonEnabled = desde.trim().length > 0 || hasta.trim().length > 0;

  const handleFilter = () => {
    // Aquí podrías añadir una validación de formato de fecha antes de enviar
    onFilter({ desde, hasta });
    onClose();
  };

  return (
    <Modal 
      visible={visible} 
      transparent 
      animationType="fade"
      onRequestClose={onClose}
    >
      <Pressable style={styles.overlay} onPress={onClose}>
        <KeyboardAvoidingView
          behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
          style={styles.keyboardView}
        >
          {/* Pressable interno vacío para evitar que clics dentro del modal lo cierren */}
          <Pressable style={styles.modalContainer} onPress={(e) => e.stopPropagation()}>
            {/* Botón de cerrar */}
            <TouchableOpacity 
              style={styles.closeButton} 
              onPress={onClose}
              hitSlop={{ top: 10, bottom: 10, left: 10, right: 10 }}
            >
              <Ionicons name="close" size={32} color={COLORS.primary} />
            </TouchableOpacity>

            <Text style={styles.label}>Filtrar desde</Text>
            <View style={styles.inputContainer}>
              <TextInput
                style={styles.input}
                placeholder="DD / MM / AAAA"
                placeholderTextColor={COLORS.inputText + '70'}
                value={desde}
                onChangeText={setDesde}
                keyboardType="numeric" // Útil para fechas
              />
              <Ionicons name="calendar-outline" size={28} color={COLORS.primary} />
            </View>

            <Text style={styles.label}>Hasta</Text>
            <View style={styles.inputContainer}>
              <TextInput
                style={styles.input}
                placeholder="DD / MM / AAAA"
                placeholderTextColor={COLORS.inputText + '70'}
                value={hasta}
                onChangeText={setHasta}
                keyboardType="numeric"
              />
              <Ionicons name="calendar-outline" size={28} color={COLORS.primary} />
            </View>

            <TouchableOpacity
              style={[
                styles.filterBtn, 
                isButtonEnabled ? styles.btnEnabled : styles.btnDisabled
              ]}
              disabled={!isButtonEnabled}
              onPress={handleFilter}
              activeOpacity={0.8}
            >
              <Text style={styles.filterBtnText}>Filtrar</Text>
            </TouchableOpacity>
          </Pressable>
        </KeyboardAvoidingView>
      </Pressable>
    </Modal>
  );
};

const styles = StyleSheet.create({
  overlay: { 
    flex: 1, 
    backgroundColor: 'rgba(30, 58, 95, 0.6)', // Azul primario con transparencia
    justifyContent: 'center', 
    alignItems: 'center' 
  },
  keyboardView: {
    width: '100%',
    alignItems: 'center',
  },
  modalContainer: { 
    width: '85%', 
    backgroundColor: COLORS.background, 
    borderRadius: 45, 
    padding: 25, 
    paddingTop: 15,
    alignItems: 'center', 
    elevation: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 5 },
    shadowOpacity: 0.25,
    shadowRadius: 10,
  },
  closeButton: { 
    alignSelf: 'flex-end', 
    marginBottom: 5 
  },
  label: { 
    alignSelf: 'flex-start', 
    fontSize: 18, 
    color: COLORS.primary, 
    fontWeight: 'bold', 
    marginLeft: 15, 
    marginBottom: 8 
  },
  inputContainer: { 
    flexDirection: 'row', 
    backgroundColor: COLORS.inputBackground, 
    width: '100%', 
    height: 55, 
    borderRadius: 30, 
    alignItems: 'center', 
    paddingHorizontal: 20, 
    marginBottom: 20 
  },
  input: { 
    flex: 1, 
    fontSize: 18, 
    color: COLORS.inputText 
  },
  filterBtn: { 
    width: '100%', 
    height: 65, 
    borderRadius: 35, 
    justifyContent: 'center', 
    alignItems: 'center', 
    marginTop: 10,
    marginBottom: 10
  },
  btnDisabled: { 
    backgroundColor: COLORS.disabled 
  },
  btnEnabled: { 
    backgroundColor: COLORS.primary 
  },
  filterBtnText: { 
    color: COLORS.buttonLight, 
    fontSize: 28, 
    fontWeight: 'bold' 
  },
});

export default FilterModal;