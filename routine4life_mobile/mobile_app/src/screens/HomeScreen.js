import React, { useState } from 'react';
import { 
  View, 
  Text, 
  StyleSheet, 
  TouchableOpacity, 
  ScrollView, 
  Platform 
} from 'react-native';
import { SafeAreaView, useSafeAreaInsets } from 'react-native-safe-area-context';
import { Ionicons, MaterialCommunityIcons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';
import FilterModal from '../components/FilterModal';
import CustomDrawer from '../componentes/CustomDrawer';

const HomeScreen = ({ navigation }) => {
  const insets = useSafeAreaInsets();
  const [modalVisible, setModalVisible] = useState(false);
  const handleNotImplemented = (feature) => alert(`${feature} próximamente disponible`);
  const handleFilterApply = (data) => {
    console.log("Filtros aplicados:", data);
  };

  return (
    <SafeAreaView style={styles.container} edges={['top', 'left', 'right']}>
      {/* --- HEADER --- */}
      <View style={styles.safeHeader}>
        <View style={styles.headerContent}>
          <TouchableOpacity onPress={() => navigation.openDrawer()}>
            hitSlop={{ top: 10, bottom: 10, left: 10, right: 10 }}
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

          <TouchableOpacity 
            style={styles.addButton} 
            onPress={() => handleNotImplemented('Agregar registro')}
            activeOpacity={0.7}
          >
            <Ionicons name="add" size={35} color={COLORS.buttonLight} />
          </TouchableOpacity>
        </View>

        <Text style={styles.selectionLabel}>Seleccionar medida</Text>
        <TouchableOpacity style={styles.selectorWrapper} onPress={() => handleNotImplemented('Selector')}>
          <Text style={styles.selectorText}>Peso corporal</Text>
          <Ionicons name="caret-down" size={20} color={COLORS.primary} />
        </TouchableOpacity>

        {/* Simulación de Gráfico */}
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

      {/* --- BOTÓN MÉDICO (FAB) --- */}
      <TouchableOpacity 
        style={[styles.fabMedical, { bottom: Math.max(16, insets.bottom + 8) }]} 
        onPress={() => handleNotImplemented('Agendar cita')}
        activeOpacity={0.8}
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
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: COLORS.background },
  safeHeader: {
    backgroundColor: COLORS.background,
    // Sombra sutil para separar el header del contenido al hacer scroll
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 2 }, shadowOpacity: 0.1, shadowRadius: 2 },
      android: { elevation: 4 },
    }),
  },
  headerContent: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingVertical: 10,
  },
  logoContainer: { flexDirection: 'row', alignItems: 'center' },
  logoTextMain: { fontSize: 24, fontWeight: 'bold', color: COLORS.primary },
  logoTextSub: { fontSize: 24, fontWeight: 'bold', color: '#2E7D5E' },
  scrollContent: { paddingHorizontal: 25, paddingBottom: 120 },
  mainTitle: { fontSize: 38, fontWeight: 'bold', color: COLORS.primary, textAlign: 'center', marginVertical: 20 },
  toolsRow: { flexDirection: 'row', justifyContent: 'space-around', alignItems: 'center', marginBottom: 25 },
  toolItem: { flexDirection: 'row', alignItems: 'center' },
  toolLabel: { fontSize: 16, color: COLORS.primary, fontWeight: 'bold', marginLeft: 5 },
  addButton: { 
    backgroundColor: COLORS.primary, 
    width: 50, 
    height: 50, 
    borderRadius: 25, 
    justifyContent: 'center', 
    alignItems: 'center',
    elevation: 4
  },
  selectionLabel: { fontSize: 18, color: COLORS.primary, textAlign: 'center', marginBottom: 10 },
  selectorWrapper: { 
    backgroundColor: COLORS.inputBackground, 
    flexDirection: 'row', 
    justifyContent: 'center', 
    alignItems: 'center', 
    paddingVertical: 12, 
    borderRadius: 30, 
    marginBottom: 20 
  },
  selectorText: { fontSize: 17, color: COLORS.primary, fontWeight: '500', marginRight: 10 },
  chartContainer: { 
    backgroundColor: '#FFFFFF', 
    height: 300, 
    borderRadius: 15, 
    padding: 15, 
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 2 }, shadowOpacity: 0.1, shadowRadius: 4 },
      android: { elevation: 3 },
    }),
  },
  chartPlaceholder: { flex: 1, borderLeftWidth: 1.5, borderBottomWidth: 1.5, borderColor: '#DDD' },
  barContainer: { flexDirection: 'row', justifyContent: 'space-around', alignItems: 'flex-end', height: '100%', paddingHorizontal: 5 },
  bar: { width: '15%', borderTopLeftRadius: 4, borderTopRightRadius: 4, alignItems: 'center' },
  barVal: { fontSize: 10, color: '#666', position: 'absolute', top: -18, fontWeight: 'bold' },
  expandIcon: { position: 'absolute', bottom: 15, left: 15 },
  fabMedical: {
    position: 'absolute',
    bottom: 30,
    right: 25,
    backgroundColor: COLORS.primary,
    width: 70,
    height: 70,
    borderRadius: 18,
    justifyContent: 'center',
    alignItems: 'center',
    elevation: 10,
    shadowColor: '#000',
    shadowOpacity: 0.3,
    shadowRadius: 5,
    shadowOffset: { width: 0, height: 4 },
  },
  plusBadge: {
    position: 'absolute',
    top: 22,
    backgroundColor: 'white',
    width: 16,
    height: 16,
    borderRadius: 4,
    justifyContent: 'center',
    alignItems: 'center',
  }
});

export default HomeScreen;