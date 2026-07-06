import api from "./api";

export const generateRoadmap = async (data) => {
  const response = await api.post("/roadmap/generate", data);
  return response.data;
};