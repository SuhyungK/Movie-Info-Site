import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexView from '@/views/IndexView'
import LoginView from '@/views/LoginView'
import ProfileView from '@/views/ProfileView'
import MyMovieView from '@/views/MyMovieView'
import SearchMovieView from '@/views/SearchMovieView'
import TicketingView from '@/views/TicketingView'
import MovieDetailView from '@/views/MovieDetailView'
import SignUpView from '@/views/SignUpView'

import TmpView from '@/views/TmpView'
import TmpReviewC from '@/views/TmpReviewC'
import store from '@/store/index.js'

Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'IndexView',
    component: IndexView
  },
  {
    path: '/Login',
    name: 'LoginView',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (store.getters.isLogin) {
        next({name: 'IndexView'})
      } else {
        next()
      }
    }
  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/mymovie',
    name: 'MyMovieView',
    component: MyMovieView
  },
  {
    path: '/search',
    name: 'SearchMovieView',
    component: SearchMovieView
  },
  {
    path: '/moviedetail',
    name: 'MovieDetailView',
    component: MovieDetailView,
  },
  {
    path: '/ticketing',
    name: 'TicketingView',
    component: TicketingView
  },
  {
    path: '/sign-up',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/tmp',
    name: 'TmpView',
    component: TmpView
  },
  {
    path: '/tmp/c',
    name: 'TmpReviewC',
    component: TmpReviewC

  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  // 접근 권한 여부(로그인 상태면 true, 비로그인 상태면 false)
  const authenticationState = store?.state?.token? true : false
  
  // 이동할 사이트가 권한을 필요로 하는 사이트인 경우
  const authentication = ['SignUpView', 'LoginView'].includes(to.name)? false: true

  console.log('authenticationState', authenticationState)
  console.log('authentication', authentication)

  console.log(from, to)
  // 비로그인 상태 && 이동하려는 이동할 사이트가 로그인 해야만 하는 사이트인 경우 
  if (!authenticationState && authentication) {
    next({name: 'LoginView'})
  }
  else if (to != from) {
    next()
  }

})


export default router
