import { Routes } from '@angular/router';
import { App } from './app';
import { LayoutComponent } from './layout/layout';

export const routes: Routes = [
  {
    path: '',
    component: App,
    children: [
      {
        path: '',
        component: LayoutComponent,
        children: [
          {
            path: 'dashboard',
            loadComponent: () => import('./pages/dashboard/dashboard').then(m => m.DashboardComponent)
          },
          {
            path: 'analyze',
            loadComponent: () => import('./pages/analyze/analyze').then(m => m.AnalyzeComponent)
          },
          {
            path: 'history',
            loadComponent: () => import('./pages/history/history').then(m => m.HistoryComponent)
          }
        ]
      },
      {
        path: '',
        redirectTo: 'dashboard',
        pathMatch: 'full'
      }
    ]
  }
];
