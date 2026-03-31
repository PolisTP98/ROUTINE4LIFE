import React, { useState } from 'react';
import { View, Text, StyleSheet, Modal, TouchableOpacity, TextInput } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';

const FilterModal = ({ visible, onClose, onFilter }) => {
  const [desde, setDesde] = useState('');
  const [hasta, setHasta] = useState('');

  // El botón se habilita si cualquiera de los dos campos tiene texto
  const isButtonEnabled = desde.trim().length > 0 || hasta.trim().length > 0;

  const handleFilter = () => {
    onFilter({ desde, hasta });
    onClose();
  };

  return (
    <Modal visible={visible} transparent animationType="fade">
      <View style={styles.overlay}>
        <View style={styles.modalContainer}>
          {/* Botón de cerrar */}
          <TouchableOpacity style={styles.closeButton} onPress={onClose}>
            <Ionicons name="close" size={30} color={COLORS.primary} />
          </TouchableOpacity>

          <Text style={styles.label}>Filtrar desde</Text>
          <View style={styles.inputContainer}>
            <TextInput
              style={styles.input}
              placeholder="DD / MM / AAAA"
              placeholderTextColor={COLORS.inputText + '70'}
              value={desde}
              onChangeText={setDesde}
            />
            <Ionicons name="calendar-outline" size={32} color={COLORS.primary} />
          </View>

          <Text style={styles.label}>Hasta</Text>
          <View style={styles.inputContainer}>
            <TextInput
              style={styles.input}
              placeholder="DD / MM / AAAA"
              placeholderTextColor={COLORS.inputText + '70'}
              value={hasta}
              onChangeText={setHasta}
            />
            <Ionicons name="calendar-outline" size={32} color={COLORS.primary} />
          </View>

          {/* Botón Filtrar con lógica de habilitación */}
          <TouchableOpacity
            style={[styles.filterBtn, isButtonEnabled ? styles.btnEnabled : styles.btnDisabled]}
            disabled={!isButtonEnabled}
            onPress={handleFilter}
          >
            <Text style={styles.filterBtnText}>Filtrar</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  overlay: { flex: 1, backgroundColor: 'rgba(0,0,0,0.4)', justifyContent: 'center', alignItems: 'center' },
  modalContainer: { width: '85%', backgroundColor: '#F5F0E8', borderRadius: 45, padding: 25, alignItems: 'center', elevation: 5 },
  closeButton: { alignSelf: 'flex-end', marginBottom: 10 },
  label: { alignSelf: 'flex-start', fontSize: 20, color: COLORS.primary, fontWeight: '500', marginLeft: 15, marginBottom: 5 },
  inputContainer: { flexDirection: 'row', backgroundColor: '#D4D4D4', width: '100%', height: 55, borderRadius: 30, alignItems: 'center', paddingHorizontal: 20, marginBottom: 20 },
  input: { flex: 1, fontSize: 18, color: COLORS.inputText },
  filterBtn: { width: '100%', height: 65, borderRadius: 35, justifyContent: 'center', alignItems: 'center', marginTop: 10 },
  btnDisabled: { backgroundColor: '#4A4A4A' },
  btnEnabled: { backgroundColor: COLORS.primary },
  filterBtnText: { color: COLORS.buttonLight, fontSize: 32, fontWeight: 'bold' },
});

export default FilterModal;