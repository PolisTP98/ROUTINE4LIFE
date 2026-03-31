import React from 'react';
import { View, Text, StyleSheet, Modal, TouchableOpacity } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';

const ErrorModal = ({ visible, message, onClose }) => {
  return (
    <Modal 
      animationType="fade" 
      transparent={true} 
      visible={visible}
      onRequestClose={onClose}
    >
      <View style={styles.overlay}>
        <View style={styles.modalCard}>
          {/* Icono de advertencia en rojo error */}
          <Ionicons name="alert-circle" size={65} color={COLORS.error} />
          
          <Text style={styles.title}>Error</Text>
          
          <Text style={styles.message}>{message}</Text>

          {/* Botón Aceptar siempre en rojo error */}
          <TouchableOpacity 
            style={styles.button} 
            onPress={onClose}
            activeOpacity={0.8}
          >
            <Text style={styles.buttonText}>Aceptar</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  overlay: { 
    flex: 1, 
    backgroundColor: 'rgba(0,0,0,0.6)', 
    justifyContent: 'center', 
    alignItems: 'center' 
  },
  modalCard: { 
    width: '85%', 
    backgroundColor: '#FAF7F2', 
    borderRadius: 45, // Bordes muy redondeados según tus capturas
    padding: 30, 
    alignItems: 'center', 
    elevation: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 5 },
    shadowOpacity: 0.3,
    shadowRadius: 6,
  },
  title: { 
    fontSize: 30, 
    fontWeight: 'bold', 
    color: COLORS.error, 
    marginVertical: 10 
  },
  message: { 
    fontSize: 18, 
    color: COLORS.primary, // Azul marino para el texto del mensaje
    textAlign: 'center', 
    marginBottom: 30, 
    fontWeight: '500',
    lineHeight: 24
  },
  button: { 
    width: '100%', 
    height: 60, 
    backgroundColor: COLORS.error, 
    borderRadius: 30, 
    justifyContent: 'center', 
    alignItems: 'center' 
  },
  buttonText: { 
    color: 'white', 
    fontSize: 22, 
    fontWeight: 'bold' 
  },
});

export default ErrorModal;