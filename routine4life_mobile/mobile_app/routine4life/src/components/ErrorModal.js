import React from 'react';
import { 
  View, 
  Text, 
  StyleSheet, 
  Modal, 
  TouchableOpacity, 
  Dimensions,
  Platform 
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';

const { width } = Dimensions.get('window');

const ErrorModal = ({ visible, message, onClose }) => {
  return (
    <Modal 
      animationType="fade" 
      transparent={true} 
      visible={visible}
      onRequestClose={onClose}
      statusBarTranslucent={true} // Hace que el overlay cubra también la barra de estado en Android
    >
      <View style={styles.overlay}>
        <View style={styles.modalCard}>
          {/* Icono de advertencia - Usamos alert-circle para consistencia visual */}
          <View style={styles.iconContainer}>
            <Ionicons name="alert-circle" size={80} color={COLORS.error} />
          </View>
          
          <Text style={styles.title}>Error</Text>
          
          <Text style={styles.message}>{message}</Text>

          {/* Botón Aceptar */}
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
    backgroundColor: 'rgba(30, 58, 95, 0.7)', // Usamos tu azul primario con transparencia para el fondo
    justifyContent: 'center', 
    alignItems: 'center',
    paddingHorizontal: 20
  },
  modalCard: { 
    width: width * 0.85, 
    backgroundColor: COLORS.buttonLight, // Tu color crema #FAF7F2
    borderRadius: 45, 
    paddingTop: 40,
    paddingBottom: 30,
    paddingHorizontal: 25, 
    alignItems: 'center', 
    ...Platform.select({
      ios: {
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 10 },
        shadowOpacity: 0.3,
        shadowRadius: 15,
      },
      android: {
        elevation: 20,
      },
    }),
  },
  iconContainer: {
    marginBottom: 10,
  },
  title: { 
    fontSize: 32, 
    fontWeight: 'bold', 
    color: COLORS.error, 
    marginBottom: 15 
  },
  message: { 
    fontSize: 18, 
    color: COLORS.primary, 
    textAlign: 'center', 
    marginBottom: 35, 
    fontWeight: '500',
    lineHeight: 26
  },
  button: { 
    width: '100%', 
    height: 65, 
    backgroundColor: COLORS.error, 
    borderRadius: 35, 
    justifyContent: 'center', 
    alignItems: 'center',
    // Sombra interna o inferior para el botón
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
    elevation: 5
  },
  buttonText: { 
    color: 'white', 
    fontSize: 24, 
    fontWeight: 'bold' 
  },
});

export default ErrorModal;