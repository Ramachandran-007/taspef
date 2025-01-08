import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import './index.css'

import Home from './views/Home.vue'
import BoardOfDirectors from './views/BoardOfDirectors.vue'
import AGMReports from './views/AGMReports.vue'
import PDFViewer from './views/PDFViewer.vue'
import Magazine from './views/Magazine.vue'
import Members from './views/Members.vue'
import AGMReportDetail from './views/AGMReportDetail.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/board', component: BoardOfDirectors },
    { path: '/agm-reports', component: AGMReports },
    { path: '/agm-report-detail/:id',name: 'agm-detail',component: AGMReportDetail,props: true },

    { path: '/pdf-viewer', name: 'pdf-viewer', component: PDFViewer },
    { path: '/magazine', component: Magazine },
    { path: '/members', component: Members },
  ]
})

const app = createApp(App)
app.use(router)
app.mount('#app')