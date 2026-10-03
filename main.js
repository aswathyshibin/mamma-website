document.addEventListener('DOMContentLoaded', () => {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const menuItems = document.querySelectorAll('.menu-item');
  const menuGrid = document.getElementById('menu-grid');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      // Remove active class from all buttons
      filterBtns.forEach(b => b.classList.remove('active'));
      // Add active class to clicked button
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');

      // Shuffle animation logic
      menuItems.forEach(item => {
        item.classList.remove('shuffle-in');
        item.classList.add('shuffle-out');
      });

      setTimeout(() => {
        menuItems.forEach(item => {
          if (filterValue === 'all' || item.getAttribute('data-category') === filterValue) {
            item.classList.remove('hidden');
            // Small delay to allow display block to apply before animation
            setTimeout(() => {
              item.classList.remove('shuffle-out');
              item.classList.add('shuffle-in');
            }, 50);
          } else {
            item.classList.add('hidden');
          }
        });
      }, 400); // Matches CSS transition time
    });
  });
});
