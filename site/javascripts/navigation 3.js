// 自定义导航折叠功能
document.addEventListener('DOMContentLoaded', function() {
    console.log('Navigation script loaded');
    
    // 为所有嵌套导航项添加点击事件
    const nestedNavItems = document.querySelectorAll('.md-nav__item--nested > .md-nav__link');
    
    nestedNavItems.forEach(function(link) {
        link.addEventListener('click', function(e) {
            // 阻止默认链接行为
            e.preventDefault();
            
            // 找到对应的复选框
            const toggle = this.parentElement.querySelector('.md-nav__toggle');
            if (toggle) {
                // 切换复选框状态
                toggle.checked = !toggle.checked;
                console.log('Toggled navigation item:', this.textContent.trim(), 'New state:', toggle.checked);
            }
        });
    });
    
    // 添加键盘支持
    nestedNavItems.forEach(function(link) {
        link.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                const toggle = this.parentElement.querySelector('.md-nav__toggle');
                if (toggle) {
                    toggle.checked = !toggle.checked;
                }
            }
        });
        
        // 添加tabindex使其可以被键盘聚焦
        link.setAttribute('tabindex', '0');
    });
});
