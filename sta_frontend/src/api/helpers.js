// src/api/index.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'https://api.example.com',
  headers: {
    'Content-Type': 'application/json'
  }
});

export const fetchData = async () => {
  const response = await apiClient.get('/data');
  return response.data;
};
