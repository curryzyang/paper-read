(function () {
  if (!window.$docsify) {
    return;
  }

  if (window.marked && window.marked.setOptions) {
    var baseOptions = {};
    if (typeof window.marked.getDefaults === "function") {
      baseOptions = window.marked.getDefaults();
    } else if (typeof window.marked.getOptions === "function") {
      baseOptions = window.marked.getOptions();
    }
    window.marked.setOptions(
      Object.assign({}, baseOptions, {
        gfm: true,
        breaks: false,
        tables: true,
        sanitize: false,
        mangle: false,
        headerIds: false,
      }),
    );
  }

  window.$docsify.plugins = window.$docsify.plugins || [];
  window.$docsify.plugins.push(function (hook, _vm) {
    hook.beforeEach(function (content) {
      if (!content) {
        return content;
      }
      var firstLine = content.split("\n")[0].trim();
      if (firstLine.startsWith("# ")) {
        return content;
      }
      return content;
    });

    hook.doneEach(function () {
      var body = document.body;
      var toc = document.querySelector(".sidebar");
      if (toc && toc.getAttribute("data-init") !== "1") {
        toc.setAttribute("data-init", "1");
      }
      if (body) {
        body.classList.add("dpr-ready");
      }
    });

    hook.mounted(function () {
      var el = document.querySelector("#app");
      if (el) {
        el.classList.add("dpr-app");
      }
    });
  });
})();
