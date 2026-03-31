import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { DrawerContentScrollView, DrawerItemList } from '@react-navigation/drawer';
import { Ionicons, MaterialCommunityIcons, FontAwesome5 } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';

const CustomDrawer = (props) => {
  return (
    <DrawerContentScrollView {...props} contentContainerStyle={styles.container}>
      {/* Header del Menu con Logo */}
      <View style={styles.header}>
        <Text style={styles.logoMain}>ROUTINE<Text style={styles.logoSub}>4LIFE</Text></Text>
        <Ionicons name="person-circle-outline" size={45} color={COLORS.primary} />
      </View>

      {/* Lista de Items */}
      <View style={styles.drawerItems}>
        <DrawerItem 
          label="Mis registros" 
          icon="home" 
          active 
          onPress={() => props.navigation.navigate('Home')} 
        />
        <DrawerItem 
          label="Citas médicas" 
          icon="medical-bag" 
          isMaterial 
          onPress={() => {}} 
        />
        <DrawerItem 
          label="Notificaciones" 
          icon="notifications" 
          onPress={() => {}} 
        />

        <Text style={styles.sectionTitle}>Rutinas</Text>
        
        <DrawerItem 
          label="Medicación" 
          icon="bandage" 
          isMaterial 
          onPress={() => {}} 
        />
        <DrawerItem 
          label="Ejercicio" 
          icon="shopping-bag" 
          isMaterial 
          onPress={() => {}} 
        />
        <DrawerItem 
          label="Alimentación" 
          icon="utensils" 
          isFontAwesome 
          onPress={() => {}} 
        />
      </View>

      {/* Footer del Menu */}
      <View style={styles.footer}>
        <DrawerItem label="Configuración" icon="settings-sharp" onPress={() => {}} />
        <DrawerItem label="Ayuda" icon="help-circle" onPress={() => {}} />
      </View>
    </DrawerContentScrollView>
  );
};

// Componente auxiliar para cada opción del menú
const DrawerItem = ({ label, icon, onPress, active, isMaterial, isFontAwesome }) => (
  <TouchableOpacity 
    style={[styles.itemWrapper, active && styles.activeItem]} 
    onPress={onPress}
  >
    <View style={styles.iconContainer}>
      {isMaterial ? (
        <MaterialCommunityIcons name={icon} size={28} color={active ? 'white' : COLORS.primary} />
      ) : isFontAwesome ? (
        <FontAwesome5 name={icon} size={24} color={active ? 'white' : COLORS.primary} />
      ) : (
        <Ionicons name={icon} size={28} color={active ? 'white' : COLORS.primary} />
      )}
    </View>
    <Text style={[styles.itemLabel, active && styles.activeLabel]}>{label}</Text>
  </TouchableOpacity>
);

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#F5F0E8' },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingVertical: 30,
  },
  logoMain: { fontSize: 24, fontWeight: 'bold', color: COLORS.primary },
  logoSub: { color: '#2E7D5E' },
  drawerItems: { flex: 1, paddingHorizontal: 10 },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: COLORS.primary,
    marginLeft: 15,
    marginTop: 25,
    marginBottom: 10,
  },
  itemWrapper: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 12,
    paddingHorizontal: 15,
    borderRadius: 30,
    marginVertical: 4,
  },
  activeItem: { backgroundColor: '#D68251' }, // Color naranja de la imagen
  iconContainer: { width: 40, alignItems: 'center' },
  itemLabel: { fontSize: 18, fontWeight: '500', color: COLORS.primary, marginLeft: 10 },
  activeLabel: { color: 'white' },
  footer: {
    paddingHorizontal: 10,
    paddingBottom: 30,
    borderTopWidth: 1,
    borderTopColor: '#E0E0E0',
    marginTop: 20,
  }
});

export default CustomDrawer;