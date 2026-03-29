// src/screens/HomeScreen.js
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { COLORS } from '../styles/theme';

const HomeScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>¡Bienvenido a la Home!</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: COLORS.background,
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    fontSize: 24,
    color: COLORS.primary,
    fontWeight: 'bold',
  },
});

export default HomeScreen;