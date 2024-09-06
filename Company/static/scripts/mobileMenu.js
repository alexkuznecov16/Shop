const menu = document.querySelector('.mobile');

const openMenu = () => {
	menu.classList.add('open');
	document.body.style.overflow = 'hidden';
};

const closeMenu = () => {
	menu.classList.remove('open');
	document.body.style.overflow = '';
};
