import React, { useEffect, useRef, useState } from 'react';
import { Animated, Text, StyleSheet, Platform, Dimensions } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { COLORS } from '../styles/theme';

const { width } = Dimensions.get('window');

const SuccessToast = ({ visible, message, onHide }) => {
  const insets = useSafeAreaInsets();
  const slideAnim = useRef(new Animated.Value(-200)).current;
  const [shouldRender, setShouldRender] = useState(visible);

  // El Toast aparecerá justo debajo del notch/status bar
  const TOP_POSITION = Platform.OS === 'ios' ? insets.top + 10 : 20;

  useEffect(() => {
    if (visible) {
      setShouldRender(true);
      Animated.spring(slideAnim, {
        toValue: TOP_POSITION,
        friction: 8,
        tension: 40,
        useNativeDriver: true,
      }).start();

      const timer = setTimeout(() => {
        handleHide();
      }, 4000); // 4 segundos es el estándar ideal

      return () => clearTimeout(timer);
    }
  }, [visible]);

  const handleHide = () => {
    Animated.timing(slideAnim, {
      toValue: -200,
      duration: 400,
      useNativeDriver: true,
    }).start(() => {
      setShouldRender(false);
      if (onHide) onHide();
    });
  };

  if (!shouldRender) return null;

  return (
    <Animated.View 
      style={[
        styles.toast, 
        { transform: [{ translateY: slideAnim }] }
      ]}
    >
      <Text style={styles.text}>{message}</Text>
    </Animated.View>
  );
};

const styles = StyleSheet.create({
  toast: {
    position: 'absolute',
    left: width * 0.05,
    right: width * 0.05,
    backgroundColor: COLORS.success,
    paddingVertical: 18,
    paddingHorizontal: 25,
    borderRadius: 35,
    zIndex: 9999, // Máxima prioridad visual
    elevation: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.35,
    shadowRadius: 6,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 1,
    borderColor: 'rgba(255,255,255,0.2)',
  },
  text: { 
    color: '#FFFFFF', 
    fontSize: 17, 
    fontWeight: 'bold', 
    textAlign: 'center',
    letterSpacing: 0.5
  },
});

export default SuccessToast;