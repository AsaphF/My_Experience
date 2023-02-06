# My_Experience
A diary of my daily experience working has a software engineer. 
I am making this diary to make a register of all things that i am building because the company that i am working on do not use GITHUb.

- January : 
 * I made a modal whiht statistics data using Vue.js (1 week)
 * I createad a project used for the employes, a personal agenda with a calendar. I used Vue.js and the FullCalendar Lib
 
 - February :
 - 03/02 -> Fiz um cálculo estatístico medindo a média do total dos usuários dos últimos 6 meses para ter um cálculo diários como referência das entradas diárias dos clientes.
  código Exemplo:
  
  user() {
      // Totais dos Clientes
      // this.totalPaid = this.users.filter(user => user.pagarmePaymentStatus === 'Pago').length
      // this.totalUnpaid = this.users.filter(user => user.pagarmePaymentStatus === 'Inadimplente').length
      // this.totalClients = this.totalPaid + this.totalUnpaid
      // this.totalCanceled = this.users.filter(user => user.pagarmePaymentStatus === 'Cancelado').length
      // this.totalNewUsersPaid = this.users.filter(user => user.pagarmePaymentStatus === 'Pago' && moment(user.createdAt).format('MM/YYYY') === moment(new Date()).format('MM/YYYY'))
      // this.totalNewUsersUnpaid = this.users.filter(user => user.pagarmePaymentStatus === 'Inadimplente' && moment(user.createdAt).format('MM/YYYY') === moment(new Date()).format('MM/YYYY'))
      // this.totalNewCancellations = this.subscriptions.filter(user => user.status === 'Cancelado' && moment(new Date()).format('MM/YYYY') === moment(new Date(user.createdAt)).format('MM/YYYY')).length

      // Cálculo da média dos dias dos ultimos 6 meses - Pagos, Inadimplentes e Cancelados
      let totalOfLastSixMonths = 0
      let lastSixMonthsPaid = 0
      let lastSixMonthsUnpaid = 0
      let totalSixMonthsCanceled = 0

      for (let i = 1; i <= 6; i++) {
        for (let l = 0; l < this.users.length; l++) {
          if (moment(new Date(this.users[l].createdAt)).format('MM/YYYY') === moment(new Date()).subtract(i, 'month').format('MM/YYYY') && this.users[l].status === 'Pago') {
            lastSixMonthsPaid++
          }
          if (moment(new Date(this.users[l].createdAt)).format('MM/YYYY') === moment(new Date()).subtract(i, 'month').format('MM/YYYY') && this.users[l].status === 'Inadimplente') {
            lastSixMonthsUnpaid++
          }
          if (moment(new Date(this.users[l].createdAt)).format('MM/YYYY') === moment(new Date()).subtract(i, 'month').format('MM/YYYY') && this.users[l].status === 'Cancelado') {
            totalSixMonthsCanceled++
          }
        }
      }
      totalOfLastSixMonths = lastSixMonthsPaid + lastSixMonthsUnpaid

      // Cálculo de cada dia do mês
      const usersPaidOfCurrentMonth = this.subscriptions.filter(user => user.status === 'Pago' && moment(new Date()).format('MM/YYYY') === moment(new Date(user.createdAt)).format('MM/YYYY')).length
      const usersUnpaidOfCurrentMonth = this.subscriptions.filter(user => user.status === 'Inadimplente' && moment(new Date()).format('MM/YYYY') === moment(new Date(user.createdAt)).format('MM/YYYY')).length
      const usersCanceledOfCurrentMonth = this.subscriptions.filter(user => user.status === 'Cancelado' && moment(new Date()).format('MM/YYYY') === moment(new Date(user.createdAt)).format('MM/YYYY')).length
      const thisMonthUsers = usersPaidOfCurrentMonth + usersUnpaidOfCurrentMonth
      const oneDay = ((totalOfLastSixMonths / 6) / 30)
      const oneDayCanceled = ((totalSixMonthsCanceled / 6) / 30)
      const oneDayUnpaid = ((lastSixMonthsUnpaid / 6) / 30)
      const lastsMonthsUsers = oneDay * Number(moment().format('D'))
      const lastsMonthsCanceled = oneDayCanceled * Number(moment().format('D'))
      const lastsMonthsUsersUnpaid = oneDayUnpaid * Number(moment().format('D'))

      // Incluindo nas propriedades
      this.averageUsers.currentMonthUsers = thisMonthUsers
      this.averageUsers.lastsMonthsUsers = lastsMonthsUsers
      this.averageUsers.currentMonthUsersCanceled = usersCanceledOfCurrentMonth
      this.averageUsers.lastsMonthCanceled = lastsMonthsCanceled
      this.averageUsers.currentMonthUsersUnpaid = usersUnpaidOfCurrentMonth
      this.averageUsers.lastsMonthUnpaid = lastsMonthsUsersUnpaid
    },
    getUsersEmissions () {
      let emissionsHistoric
- 06/02 -> Fiz ajustes em no todoList
