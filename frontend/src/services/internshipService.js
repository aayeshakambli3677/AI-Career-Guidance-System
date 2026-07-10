import api from "./api";

export const getInternships = async (data) => {
  const response = await api.post(
    "/internship/recommend",
    data
  );

  return response.data;
};