var tabs = (function () {
    return function (selector, config) {
        var _tabsContainer = (typeof selector === 'string' ? document.querySelector(selector) : selector);

        var _showTab = function (tabsLinkTarget) {
            var tabsPaneTarget, tabsLinkActive, tabsPaneShow;
            tabsPaneTarget = document.querySelector(tabsLinkTarget.getAttribute('href'));
            tabsLinkActive = tabsLinkTarget.parentElement.querySelector('.tabs__link_active');
            tabsPaneShow = tabsPaneTarget.parentElement.querySelector('.tabs__pane_show');
            // если следующая вкладка равна активной, то завершаем работу
            if (tabsLinkTarget === tabsLinkActive) {
                return;
            }
            // удаляем классы у текущих активных элементов
            if (tabsLinkActive !== null) {
                tabsLinkActive.classList.remove('tabs__link_active');
            }
            if (tabsPaneShow !== null) {
                tabsPaneShow.classList.remove('tabs__pane_show');
            }
            // добавляем классы к элементам (в завимости от выбранной вкладки)
            tabsLinkTarget.classList.add('tabs__link_active');
            tabsPaneTarget.classList.add('tabs__pane_show');
            var eventTabShow = new CustomEvent('tab.show', {bubbles: true, detail: {tabsLinkPrevious: tabsLinkActive}});
            tabsLinkTarget.dispatchEvent(eventTabShow);
        }

        var _switchTabTo = function (tabsLinkIndex) {
            var tabsLinks = _tabsContainer.querySelectorAll('.tabs__link');
            if (tabsLinks.length > 0) {
                if (tabsLinkIndex > tabsLinks.length) {
                    tabsLinkIndex = tabsLinks.length;
                } else if (tabsLinkIndex < 1) {
                    tabsLinkIndex = 1;
                }
                _showTab(tabsLinks[tabsLinkIndex - 1]);
            }
        }

        var _setupListeners = function () {
            _tabsContainer.addEventListener('click', function (e) {
                var tabsLinkTarget = e.target;
                // завершаем выполнение функции, если кликнули не по ссылке
                if (!tabsLinkTarget.classList.contains('tabs__link')) {
                    return;
                }
                // отменяем стандартное действие
                e.preventDefault();
                _showTab(tabsLinkTarget);
            });
        }

        _setupListeners();

        return {
            switchTabTo: function (index) {
                _switchTabTo(index);
            }
        }
    }
}());

tabs('.tabs');