// src/services/authService.js

import api from "./api";

export const registerUser = async (userData) => {
  const response = await api.post("/users/create", userData);
  return response.data;
};

export const loginUser = async (userData) => {
  const response = await api.post("/users/login", userData);
  return response.data;
};

export const getCurrentUser = async (token) => {
  const response = await api.get(`/users/me?token=${token}`);
  return response.data;
};