import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { DrawerContentScrollView } from '@react-navigation/drawer';
import { Ionicons, MaterialCommunityIcons, FontAwesome5 } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';

const CustomDrawer = (props) => {
  // Función para determinar si una ruta está activa
  const isRouteActive = (routeName) => {
    return props.state.routes[props.state.index].name === routeName;
  };

  return (
    <View style={{ flex: 1, backgroundColor: COLORS.background }}>
      <DrawerContentScrollView {...props} contentContainerStyle={styles.scrollContainer}>
        
        {/* Header del Menu con Logo */}
        <View style={styles.header}>
          <View style={styles.logoWrapper}>
            <Text style={styles.logoMain}>ROUTINE<Text style={styles.logoSub}>4LIFE</Text></Text>
          </View>
          <TouchableOpacity onPress={() => props.navigation.navigate('Profile')}>
            <Ionicons name="person-circle-outline" size={50} color={COLORS.primary} />
          </TouchableOpacity>
        </View>

        {/* Lista de Items */}
        <View style={styles.drawerItems}>
          <DrawerItem 
            label="Mis registros" 
            icon="home-outline" 
            active={isRouteActive('Home')} 
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
            icon="notifications-outline" 
            onPress={() => {}} 
          />

          <Text style={styles.sectionTitle}>Rutinas</Text>
          
          <DrawerItem 
            label="Medicación" 
            icon="bandage-outline" 
            isMaterial 
            onPress={() => {}} 
          />
          <DrawerItem 
            label="Ejercicio" 
            icon="dumbbell" 
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
      </DrawerContentScrollView>

      {/* Footer del Menu - Fuera del Scroll para que sea fijo */}
      <View style={styles.footer}>
        <DrawerItem label="Configuración" icon="settings-outline" onPress={() => {}} />
        <DrawerItem label="Ayuda" icon="help-circle-outline" onPress={() => {}} />
        
        <TouchableOpacity style={styles.logoutBtn} onPress={() => props.navigation.navigate('Login')}>
           <Ionicons name="log-out-outline" size={24} color={COLORS.error} />
           <Text style={styles.logoutText}>Cerrar sesión</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const DrawerItem = ({ label, icon, onPress, active, isMaterial, isFontAwesome }) => {
  const iconColor = active ? 'white' : COLORS.primary;
  
  return (
    <TouchableOpacity 
      style={[styles.itemWrapper, active && styles.activeItem]} 
      onPress={onPress}
      activeOpacity={0.7}
    >
      <View style={styles.iconContainer}>
        {isMaterial ? (
          <MaterialCommunityIcons name={icon} size={26} color={iconColor} />
        ) : isFontAwesome ? (
          <FontAwesome5 name={icon} size={22} color={iconColor} />
        ) : (
          <Ionicons name={icon} size={26} color={iconColor} />
        )}
      </View>
      <Text style={[styles.itemLabel, active && styles.activeLabel]}>{label}</Text>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  scrollContainer: { paddingTop: 10 },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingVertical: 25,
    marginBottom: 10,
  },
  logoWrapper: { flexDirection: 'row' },
  logoMain: { fontSize: 24, fontWeight: 'bold', color: COLORS.primary },
  logoSub: { color: COLORS.success || '#2E7D5E' },
  drawerItems: { paddingHorizontal: 10 },
  sectionTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: COLORS.primary,
    opacity: 0.6,
    marginLeft: 15,
    marginTop: 25,
    marginBottom: 10,
    textTransform: 'uppercase',
    letterSpacing: 1,
  },
  itemWrapper: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 12,
    paddingHorizontal: 15,
    borderRadius: 30,
    marginVertical: 2,
  },
  activeItem: { backgroundColor: '#D68251' }, // Color acento
  iconContainer: { width: 35, alignItems: 'center', justifyContent: 'center' },
  itemLabel: { fontSize: 17, fontWeight: '500', color: COLORS.primary, marginLeft: 10 },
  activeLabel: { color: 'white', fontWeight: 'bold' },
  footer: {
    paddingHorizontal: 15,
    paddingBottom: 40,
    borderTopWidth: 1,
    borderTopColor: '#E0DCD6',
    paddingTop: 10,
  },
  logoutBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 15,
    paddingHorizontal: 15,
  },
  logoutText: {
    fontSize: 16,
    color: COLORS.error,
    fontWeight: 'bold',
    marginLeft: 15,
  }
});

export default CustomDrawer;