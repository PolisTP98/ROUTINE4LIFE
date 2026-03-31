import React, { useState } from 'react'; // Se agregó useState aquí
import { View, Text, StyleSheet, TouchableOpacity, ScrollView } from 'react-native';
import { Ionicons, MaterialCommunityIcons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';
import FilterModal from '../components/FilterModal';

const HomeScreen = ({ navigation }) => {
  const [modalVisible, setModalVisible] = useState(false);
  const handleNotImplemented = (feature) => alert(`${feature} próximamente disponible`);

  const handleFilterApply = (data) => {
    console.log("Filtros aplicados:", data);
  };

  return (
    <View style={styles.container}>
      {/* --- HEADER ESTÁTICO (No se mueve con el scroll) --- */}
      <View style={styles.header}>
        <TouchableOpacity onPress={() => navigation.openDrawer()}>
          <Ionicons name="menu" size={35} color={COLORS.primary} />
        </TouchableOpacity>
        
        <View style={styles.logoContainer}>
          <Text style={styles.logoTextMain}>ROUTINE</Text>
          <Text style={styles.logoTextSub}>4LIFE</Text>
        </View>

        <TouchableOpacity onPress={() => handleNotImplemented('Perfil')}>
          <Ionicons name="person-circle-outline" size={40} color={COLORS.primary} />
        </TouchableOpacity>
      </View>

      {/* --- CONTENIDO DESLIZABLE --- */}
      <ScrollView 
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        <Text style={styles.mainTitle}>Mis registros</Text>

        <View style={styles.toolsRow}>
          <TouchableOpacity style={styles.toolItem} onPress={() => setModalVisible(true)}>
            <MaterialCommunityIcons name="filter-variant" size={28} color={COLORS.primary} />
            <Text style={styles.toolLabel}>Filtrar</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.toolItem} onPress={() => handleNotImplemented('Ver Gráfico')}>
            <MaterialCommunityIcons name="swap-vertical-variant" size={28} color={COLORS.primary} />
            <Text style={styles.toolLabel}>Gráfico</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.addButton} onPress={() => handleNotImplemented('Agregar registro')}>
            <Ionicons name="add" size={35} color={COLORS.buttonLight} />
          </TouchableOpacity>
        </View>

        <Text style={styles.selectionLabel}>Seleccionar medida</Text>
        <TouchableOpacity style={styles.selectorWrapper} onPress={() => handleNotImplemented('Selector')}>
          <Text style={styles.selectorText}>Peso corporal</Text>
          <Ionicons name="caret-down" size={20} color={COLORS.primary} />
        </TouchableOpacity>

        {/* Gráfico (Simulando la imagen subida) */}
        <View style={styles.chartContainer}>
          <View style={styles.chartPlaceholder}>
             <View style={styles.barContainer}>
                <View style={[styles.bar, {height: '80%', backgroundColor: '#E5B382'}]}><Text style={styles.barVal}>100</Text></View>
                <View style={[styles.bar, {height: '75%', backgroundColor: '#C44545'}]}><Text style={styles.barVal}>96</Text></View>
                <View style={[styles.bar, {height: '60%', backgroundColor: '#2E7D5E'}]}><Text style={styles.barVal}>80</Text></View>
                <View style={[styles.bar, {height: '70%', backgroundColor: '#4DA6A6'}]}><Text style={styles.barVal}>93</Text></View>
                <View style={[styles.bar, {height: '55%', backgroundColor: '#D68251'}]}><Text style={styles.barVal}>77</Text></View>
             </View>
          </View>
          <Ionicons name="expand-outline" size={24} color={COLORS.primary} style={styles.expandIcon} />
        </View>
      </ScrollView>

      {/* --- BOTÓN AZUL FIJO (Maletín Médico) --- */}
      <TouchableOpacity 
        style={styles.fabMedical} 
        onPress={() => handleNotImplemented('Agendar cita')}
      >
        <MaterialCommunityIcons name="medical-bag" size={35} color={COLORS.buttonLight} />
        <View style={styles.plusBadge}>
            <Ionicons name="add" size={14} color={COLORS.primary} />
        </View>
      </TouchableOpacity>

      <FilterModal 
        visible={modalVisible} 
        onClose={() => setModalVisible(false)} 
        onFilter={handleFilterApply} 
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: COLORS.background },
  header: {
    height: 110,
    backgroundColor: COLORS.background,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-end',
    paddingHorizontal: 20,
    paddingBottom: 15,
    zIndex: 10,
  },
  logoContainer: { flexDirection: 'row', alignItems: 'center' },
  logoTextMain: { fontSize: 28, fontWeight: 'bold', color: COLORS.primary },
  logoTextSub: { fontSize: 28, fontWeight: 'bold', color: '#2E7D5E' },
  scrollContent: { paddingHorizontal: 25, paddingBottom: 120 },
  mainTitle: { fontSize: 42, fontWeight: 'bold', color: COLORS.primary, textAlign: 'center', marginVertical: 30 },
  toolsRow: { flexDirection: 'row', justifyContent: 'space-around', alignItems: 'center', marginBottom: 30 },
  toolItem: { flexDirection: 'row', alignItems: 'center' },
  toolLabel: { fontSize: 18, color: COLORS.primary, fontWeight: 'bold', marginLeft: 5 },
  addButton: { backgroundColor: COLORS.primary, width: 55, height: 55, borderRadius: 28, justifyContent: 'center', alignItems: 'center', elevation: 5 },
  selectionLabel: { fontSize: 18, color: COLORS.primary, textAlign: 'center', marginBottom: 10 },
  selectorWrapper: { backgroundColor: COLORS.inputBackground, flexDirection: 'row', justifyContent: 'center', alignItems: 'center', paddingVertical: 15, borderRadius: 30, marginBottom: 20 },
  selectorText: { fontSize: 18, color: COLORS.primary, fontWeight: '500', marginRight: 10 },
  chartContainer: { backgroundColor: '#FFFFFF', height: 320, borderRadius: 15, padding: 15, elevation: 3 },
  chartPlaceholder: { flex: 1, borderLeftWidth: 2, borderBottomWidth: 2, borderColor: '#444' },
  barContainer: { flexDirection: 'row', justifyContent: 'space-around', alignItems: 'flex-end', height: '100%', paddingHorizontal: 5 },
  bar: { width: '16%', borderTopLeftRadius: 4, borderTopRightRadius: 4, alignItems: 'center' },
  barVal: { fontSize: 10, color: '#444', position: 'absolute', top: -15, fontWeight: 'bold' },
  expandIcon: { position: 'absolute', bottom: 15, left: 15 },
  fabMedical: {
    position: 'absolute',
    bottom: 40,
    right: 30,
    backgroundColor: COLORS.primary,
    width: 75,
    height: 75,
    borderRadius: 20,
    justifyContent: 'center',
    alignItems: 'center',
    elevation: 8,
  },
  plusBadge: {
    position: 'absolute',
    top: 25,
    backgroundColor: 'white',
    width: 16,
    height: 16,
    borderRadius: 4,
    justifyContent: 'center',
    alignItems: 'center',
  }
});

export default HomeScreen;