/* 号卡·中国 通用脚本 */
(function () {
  'use strict';

  /* 移动端导航开关 */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
    });
  }

  /* 给当前页面的导航链接加高亮 */
  var here = location.pathname.replace(/\/$/, '') || '/index.html';
  var links = document.querySelectorAll('.nav a');
  Array.prototype.forEach.call(links, function (a) {
    var href = a.getAttribute('href');
    if (!href) return;
    var target = href.indexOf('#') === 0 ? href.split('#')[0] : href;
    if (target === here) a.classList.add('active');
  });

  /* 首页"快速查找"输入：过滤虚拟运营商/工具列表 */
  var filterInput = document.querySelector('#quickFilter');
  if (filterInput) {
    filterInput.addEventListener('input', function () {
      var kw = filterInput.value.trim().toLowerCase();
      var items = document.querySelectorAll('[data-filter]');
      Array.prototype.forEach.call(items, function (item) {
        var text = (item.getAttribute('data-filter') || '').toLowerCase();
        item.style.display = (!kw || text.indexOf(kw) !== -1) ? '' : 'none';
      });
    });
  }

  /* 返回顶部按钮 */
  var backTop = document.querySelector('.back-top');
  if (backTop) {
    window.addEventListener('scroll', function () {
      backTop.style.display = window.scrollY > 400 ? 'block' : 'none';
    });
    backTop.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
  }
})();
