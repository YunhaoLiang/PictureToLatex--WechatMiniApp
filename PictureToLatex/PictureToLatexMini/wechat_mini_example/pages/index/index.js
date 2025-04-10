const app = getApp()

Page({
  data: {
    imageUrl: '',      // 图片路径
    latexResult: '',   // 识别结果
    isLoading: false,  // 加载状态
    errorMsg: ''       // 错误信息
  },

  onLoad() {
    // 检查网络状态
    this.checkNetwork()
  },

  // 检查网络状态
  checkNetwork() {
    wx.getNetworkType({
      success: (res) => {
        if (res.networkType === 'none') {
          this.setData({ errorMsg: '网络连接失败，请检查网络设置' })
        }
      }
    })
  },

  // 选择图片
  chooseImage() {
    if (this.data.isLoading) return

    wx.chooseImage({
      count: 1,
      sizeType: ['compressed'],
      sourceType: ['album', 'camera'],
      success: (res) => {
        const tempFilePath = res.tempFilePaths[0]
        this.setData({ 
          imageUrl: tempFilePath,
          latexResult: '',
          isLoading: true,
          errorMsg: ''
        })
        this.uploadImage(tempFilePath)
      },
      fail: (error) => {
        this.setData({
          errorMsg: '选择图片失败：' + error.errMsg
        })
      }
    })
  },

  // 上传图片
  uploadImage(filePath) {
    const apiUrl = app.getApiBaseUrl() + '/convert'
    
    wx.uploadFile({
      url: apiUrl,
      filePath: filePath,
      name: 'file',
      success: (res) => {
        try {
          if (res.statusCode === 500) {
            throw new Error('服务器内部错误')
          }
          
          const result = JSON.parse(res.data)
          if (result.code === 0) {
            this.setData({
              latexResult: result.data.latex,
              isLoading: false,
              errorMsg: ''
            })
          } else {
            this.setData({
              errorMsg: '识别失败：' + result.msg,
              isLoading: false
            })
          }
        } catch (e) {
          this.setData({
            errorMsg: '解析结果失败：' + e.message,
            isLoading: false
          })
        }
      },
      fail: (error) => {
        this.setData({
          errorMsg: '上传失败：' + error.errMsg,
          isLoading: false
        })
      }
    })
  },

  // 复制结果
  copyResult() {
    if (!this.data.latexResult) {
      this.setData({
        errorMsg: '无内容可复制'
      })
      return
    }
    
    wx.setClipboardData({
      data: this.data.latexResult,
      success: () => {
        wx.showToast({
          title: '已复制到剪贴板',
          icon: 'success'
        })
      },
      fail: () => {
        this.setData({
          errorMsg: '复制失败'
        })
      }
    })
  },

  // 清除错误信息
  clearError() {
    this.setData({
      errorMsg: ''
    })
  }
}) 