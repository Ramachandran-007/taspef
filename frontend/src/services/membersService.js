import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';

export const membersService = {
  async getAllMembers() {
    const response = await axios.get('http://127.0.0.1:8000/api/members/');
    return response.data.members;
  },
  async createMember(member) {
    const response = await axios.post('http://127.0.0.1:8000/api/members/create/', member);
    return response.data;
  }
};

