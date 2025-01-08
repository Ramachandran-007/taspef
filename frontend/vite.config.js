import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path';

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      // Resolve pdfjs-dist to the correct path
      'pdfjs-dist': path.resolve(__dirname, 'node_modules/pdfjs-dist'),
    },
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          // Separate the worker file for better optimization
          pdfWorker: ['pdfjs-dist/build/pdf.worker.mjs'],
        },
      },
    },
  },
});
