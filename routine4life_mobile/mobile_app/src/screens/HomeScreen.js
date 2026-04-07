import React, { useState, useEffect } from 'react';
import { 
  View, 
  Text, 
  StyleSheet, 
  TouchableOpacity, 
  ScrollView, 
  Platform,
  ActivityIndicator
} from 'react-native';
import { SafeAreaView, useSafeAreaInsets } from 'react-native-safe-area-context';
import { Ionicons, MaterialCommunityIcons } from '@expo/vector-icons';
import { COLORS } from '../styles/theme';
import FilterModal from '../components/FilterModal';
import { API_URL } from '../api/config'; 

const HomeScreen = ({ navigation, route }) => {
  const insets = useSafeAreaInsets();
  const [modalVisible, setModalVisible] = useState(false);
  
  const [consultas, setConsultas] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const id_paciente = route.params?.id_paciente || 1; 

  useEffect(() => {
    obtenerDatosDelPaciente();
  }, []);

  const obtenerDatosDelPaciente = async () => {
    try {
      const response = await fetch(`${API_URL}/auth-movil/${id_paciente}/consultas`);
      const data = await response.json();

      if (response.ok) {
        const consultasConPeso = data.filter(c => c.peso != null).slice(0, 5);
        setConsultas(consultasConPeso);
      } else {
        console.log("Error al cargar consultas:", data.detail);
      }
    } catch (error) {
      console.error("Error de red al cargar Home:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleNotImplemented = (feature) => alert(`${feature} próximamente disponible`);
  
  const handleFilterApply = (data) => {
    console.log("Filtros aplicados:", data);
  };

  const renderBars = () => {
    if (consultas.length === 0) {
      return <Text style={{textAlign: 'center', marginTop: 100, color: '#666'}}>No hay registros de peso aún.</Text>;
    }

    const maxPeso = Math.max(...consultas.map(c => parseFloat(c.peso)));
    const colores = ['#E5B382', '#C44545', '#2E7D5E', '#4DA6A6', '#D68251'];

    return consultas.map((consulta, index) => {
      // Regla de 3 para que la barra más alta llegue al 90% del contenedor
      const heightPercent = maxPeso > 0 ? (parseFloat(consulta.peso) / maxPeso) * 90 : 0; 
      
      return (
        <View key={consulta.id_consulta} style={[styles.bar, { height: `${heightPercent}%`, backgroundColor: colores[index % colores.length] }]}>
          <Text style={styles.barVal}>{consulta.peso}</Text>
        </View>
      );
    });
  };

  return (
    <SafeAreaView style={styles.container} edges={['top', 'left', 'right']}>
      <View style={styles.safeHeader}>
        <View style={styles.headerContent}>
          <TouchableOpacity 
            onPress={() => navigation.openDrawer()}
            hitSlop={{ top: 10, bottom: 10, left: 10, right: 10 }}
          >
            <Ionicons name="menu" size={35} color={COLORS.primary} />
          </TouchableOpacity>

          <View style={styles.logoContainer}>
            <Text style={styles.logoTextMain}>ROUTINE</Text>
            <Text style={styles.logoTextSub}>4LIFE</Text>
          </View>

          <TouchableOpacity onPress={() => navigation.navigate('Profile')}>
            <Ionicons name="person-circle-outline" size={40} color={COLORS.primary} />
          </TouchableOpacity>
        </View>
      </View>

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

        {/* Gráfico Dinámico */}
        <View style={styles.chartContainer}>
          <View style={styles.chartPlaceholder}>
             {isLoading ? (
               <ActivityIndicator size="large" color={COLORS.primary} style={{ marginTop: 100 }} />
             ) : (
               <View style={styles.barContainer}>
                 {renderBars()}
               </View>
             )}
          </View>
          <Ionicons name="expand-outline" size={24} color={COLORS.primary} style={styles.expandIcon} />
        </View>
      </ScrollView>

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