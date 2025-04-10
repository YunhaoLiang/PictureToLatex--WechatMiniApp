// app.js
App({
  globalData: {
    // 环境配置
    env: 'dev', // 'dev' 或 'prod'
    // 开发环境API地址
    dev: {
      // 模拟器使用localhost
      simulatorApiUrl: 'http://localhost:8001/api',
      // 真机使用IP地址
      deviceApiUrl: 'http://YOUR_DEVICE_IP:8001/api'
    },
    // 生产环境API地址（需要替换为实际的服务器地址）
    prod: {
      apiBaseUrl: 'https://YOUR_DOMAIN.com/api'
    }
  },
  
  onLaunch() {
    // 初始化
    console.log('小程序启动')
    
    // 检查是否是开发环境
    if (__wxConfig && __wxConfig.envVersion === 'develop') {
      console.log('当前是开发环境')
      this.globalData.env = 'dev'
    } else {
      console.log('当前是生产环境')
      this.globalData.env = 'prod'
    }
  },

  // 获取当前环境的API地址
  getApiBaseUrl() {
    if (this.globalData.env === 'prod') {
      return this.globalData.prod.apiBaseUrl
    }
    // 判断是否在模拟器中运行
    const systemInfo = wx.getSystemInfoSync()
    return systemInfo.platform === 'devtools' 
      ? this.globalData.dev.simulatorApiUrl 
      : this.globalData.dev.deviceApiUrl
  }
}) 