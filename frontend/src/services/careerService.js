import api from "./api";

export const getCareerAdvice = async (data) => {
  const response = await api.post("/career/advice", data);
  return response.data;
};

export const getSkillsSuggestion = async (data) => {
  const response = await api.post("/career/skills", data);
  return response.data;
};

export const getRoadmap = async (data) => {
  const response = await api.post("/career/roadmap", data);
  return response.data;
};