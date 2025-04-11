export default defineNuxtRouteMiddleware((to, from) => {
  const userStore = useUserStore()
  
  // Routes that require employer role
  const employerRoutes = ['/myjobs', '/createjob', '/editjob']
  
  // Routes that require jobseeker role
  const jobseekerRoutes = ['/browse']
  
  if (employerRoutes.some(route => to.path.startsWith(route)) && 
      userStore.user.userType !== 'employer') {
    return navigateTo('/login')
  }
  
  if (jobseekerRoutes.some(route => to.path.startsWith(route)) && 
      userStore.user.userType !== 'jobseeker') {
    return navigateTo('/login')
  }
}) 