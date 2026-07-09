import api from "./api";

export const generateQuestions = async () => {
  const response = await api.get("/interview/hr-questions");
  return response.data;
};
export const evaluateAnswer = async (data) => {
  const response = await api.post("/interview/evaluate", data);
  return response.data;
};