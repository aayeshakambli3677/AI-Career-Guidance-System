import api from "./api";

export const getUserProfile = async (token) => {
  const response = await api.get(
    `/users/me?token=${token}`
  );

  return response.data;
};