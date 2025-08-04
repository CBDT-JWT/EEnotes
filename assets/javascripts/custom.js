// 自定义JavaScript - 简化版本，因为我们已经override了header模板

document.addEventListener('DOMContentLoaded', function() {
    console.log('页面加载完成，检查自定义导航栏');
    
    // 确保自定义导航栏可见
    const customNav = document.querySelector('.custom-blog-nav');
    if (customNav) {
        console.log('找到自定义导航栏');
        customNav.style.display = 'flex';
    } else {
        console.log('未找到自定义导航栏');
    }
    
    // 隐藏Material主题可能残留的元素
    const tabs = document.querySelector('.md-tabs');
    if (tabs) {
        tabs.style.display = 'none';
        console.log('隐藏了Material主题的标签导航');
    }
    
    // 隐藏侧边栏中的site name（避免重复）
    const siteNameInSidebar = document.querySelector('.md-nav--primary .md-nav__title');
    if (siteNameInSidebar) {
        siteNameInSidebar.style.display = 'none';
        console.log('隐藏了侧边栏中的站点名称');
    }
});

console.log('Custom navigation script loaded');
