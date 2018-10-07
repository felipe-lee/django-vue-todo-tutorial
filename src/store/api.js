// src/store/api.js

import axios from 'axios';

export default {
  get (url, request) {
    return axios.get(url, request);
  },
  post (url, request) {
    return axios.post(url, request);
  },
  patch (url, request) {
    return axios.patch(url, request);
  },
  delete (url, request) {
    return axios.delete(url, request);
  },
};
