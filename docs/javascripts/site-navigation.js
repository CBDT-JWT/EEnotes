/* Public site navigation; course navigation and search stay with Zensical. */
(() => {
  'use strict';

  function initialize() {
    const header = document.querySelector('#landingNav');
    if (!header || header.dataset.bound) return;
    header.dataset.bound = 'true';
    const toggle = header.querySelector('.landing-nav-toggle');
    const menu = header.querySelector('.landing-nav-links');
    const label = toggle.querySelector('.visually-hidden');

    function setOpen(open) {
      toggle.setAttribute('aria-expanded', String(open));
      menu.classList.toggle('is-open', open);
      document.body.classList.toggle('nav-open', open);
      label.textContent = open ? '关闭导航' : '打开导航';
    }

    toggle.addEventListener('click', event => {
      const open = toggle.getAttribute('aria-expanded') !== 'true';
      const drawer = document.querySelector('#__drawer');
      if (open && drawer) drawer.checked = false;
      setOpen(open);
      if (open && event.detail === 0) menu.querySelector('a')?.focus();
    });
    menu.addEventListener('click', event => {
      if (event.target.closest('a')) setOpen(false);
    });
    document.addEventListener('pointerdown', event => {
      if (!header.contains(event.target)) setOpen(false);
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && menu.classList.contains('is-open')) {
        setOpen(false);
        toggle.focus();
      } else if (event.key === 'Escape' && document.querySelector('#__drawer')?.checked) {
        document.querySelector('#__drawer').checked = false;
        document.querySelector('.notes-drawer-toggle')?.focus();
      }
      if (event.key === 'Tab' && menu.classList.contains('is-open')) {
        const links = [...menu.querySelectorAll('a')];
        if (event.shiftKey && document.activeElement === toggle) {
          event.preventDefault();
          links.at(-1).focus();
        } else if (!event.shiftKey && document.activeElement === links.at(-1)) {
          event.preventDefault();
          toggle.focus();
        }
      }
    });
    window.matchMedia('(min-width: 821px)').addEventListener('change', () => setOpen(false));
    document.querySelector('.notes-drawer-toggle')?.addEventListener('keydown', event => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        document.querySelector('#__drawer').click();
      }
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initialize);
  else initialize();
  if (typeof document$ !== 'undefined') document$.subscribe(initialize);
})();
