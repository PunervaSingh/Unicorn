var normal = document.getElementById("normal");
normal.addEventListener("click", () => {
    document.querySelector("html").style.filter = "invert(0)";
    let media = document.querySelectorAll("img, picture, video");
    media.forEach((mediaItem) => {
        mediaItem.style.filter = "invert(0)"
    })
    document.querySelector("html").style.backgroundColor = "white";
    document.querySelector("body").style.backgroundColor = "white";
    document.querySelector("html").style.color= "inherit";
    document.querySelector("body").style.color= "inherit";
    document.querySelector("span").style.color= "inherit";
    const collection = document.getElementsByTagName("span");
    for (let i = 0; i < collection.length; i++) {
        collection[i].style.color = "inherit";
    }
    const divcollection = document.getElementsByTagName("div");
    for (let i = 0; i < divcollection.length; i++) {
        divcollection[i].style.color = "inherit";
        divcollection[i].style.background = "white";
    }
    const h1collection = document.getElementsByTagName("h1");
    for (let i = 0; i < h1collection.length; i++) {
        h1collection[i].style.color = "inherit";
    }
    const h2collection = document.getElementsByTagName("h2");
    for (let i = 0; i < h2collection.length; i++) {
        h2collection[i].style.color = "inherit";
    }
    const h3collection = document.getElementsByTagName("h3");
    for (let i = 0; i < h3collection.length; i++) {
        h3collection[i].style.color = "inherit";
    }
    const pcollection = document.getElementsByTagName("p");
    for (let i = 0; i < pcollection.length; i++) {
        pcollection[i].style.color = "inherit";
    }
    const acollection = document.getElementsByTagName("a");
    for (let i = 0; i < acollection.length; i++) {
        acollection[i].style.color = "#0645ad";
    }
    const tablecollection = document.getElementsByTagName("table");
    for (let i = 0; i < tablecollection.length; i++) {
        tablecollection[i].style.color = "inherit";
        tablecollection[i].style.background = "white";
    }
    const licollection = document.getElementsByTagName("li");
    for (let i = 0; i < licollection.length; i++) {
        licollection[i].style.background = "white";
    }
})

var grayscale = document.getElementById("grayscale");
grayscale.addEventListener("click", () => {
    document.querySelector("html").style.filter = "invert(0)";
    let media = document.querySelectorAll("img, picture, video");
    media.forEach((mediaItem) => {
        mediaItem.style.filter = "invert(0)"
    })
    document.querySelector("html").style.filter = "grayscale(1)";
    document.querySelector("html").style.backgroundColor = "white";
    document.querySelector("body").style.backgroundColor = "white";
    document.querySelector("html").style.color= "inherit";
    document.querySelector("body").style.color= "inherit";
    document.querySelector("span").style.color= "inherit";
    const collection = document.getElementsByTagName("span");
    for (let i = 0; i < collection.length; i++) {
        collection[i].style.color = "inherit";
    }
    const divcollection = document.getElementsByTagName("div");
    for (let i = 0; i < divcollection.length; i++) {
        divcollection[i].style.color = "inherit";
        divcollection[i].style.background = "white";
    }
    const h1collection = document.getElementsByTagName("h1");
    for (let i = 0; i < h1collection.length; i++) {
        h1collection[i].style.color = "inherit";
    }
    const h2collection = document.getElementsByTagName("h2");
    for (let i = 0; i < h2collection.length; i++) {
        h2collection[i].style.color = "inherit";
    }
    const h3collection = document.getElementsByTagName("h3");
    for (let i = 0; i < h3collection.length; i++) {
        h3collection[i].style.color = "inherit";
    }
    const pcollection = document.getElementsByTagName("p");
    for (let i = 0; i < pcollection.length; i++) {
        pcollection[i].style.color = "inherit";
    }
    const acollection = document.getElementsByTagName("a");
    for (let i = 0; i < acollection.length; i++) {
        acollection[i].style.color = "#0645ad";
    }
    const tablecollection = document.getElementsByTagName("table");
    for (let i = 0; i < tablecollection.length; i++) {
        tablecollection[i].style.color = "inherit";
        tablecollection[i].style.background = "white";
    }
    const licollection = document.getElementsByTagName("li");
    for (let i = 0; i < licollection.length; i++) {
        licollection[i].style.background = "white";
    }
})
var invertedcolour = document.getElementById("invertedcolour");
invertedcolour.addEventListener("click", () => {
    document.querySelector("html").style.filter = "invert(0)";
    let media = document.querySelectorAll("img, picture, video");
    media.forEach((mediaItem) => {
        mediaItem.style.filter = "invert(0)"
    })
    document.querySelector("html").style.backgroundColor = "white";
    document.querySelector("body").style.backgroundColor = "white";
    document.querySelector("html").style.color= "inherit";
    document.querySelector("body").style.color= "inherit";
    document.querySelector("span").style.color= "inherit";
    const collection = document.getElementsByTagName("span");
    for (let i = 0; i < collection.length; i++) {
        collection[i].style.color = "inherit";
    }
    const divcollection = document.getElementsByTagName("div");
    for (let i = 0; i < divcollection.length; i++) {
        divcollection[i].style.color = "inherit";
        divcollection[i].style.background = "white";
    }
    const h1collection = document.getElementsByTagName("h1");
    for (let i = 0; i < h1collection.length; i++) {
        h1collection[i].style.color = "inherit";
    }
    const h2collection = document.getElementsByTagName("h2");
    for (let i = 0; i < h2collection.length; i++) {
        h2collection[i].style.color = "inherit";
    }
    const h3collection = document.getElementsByTagName("h3");
    for (let i = 0; i < h3collection.length; i++) {
        h3collection[i].style.color = "inherit";
    }
    const pcollection = document.getElementsByTagName("p");
    for (let i = 0; i < pcollection.length; i++) {
        pcollection[i].style.color = "inherit";
    }
    const acollection = document.getElementsByTagName("a");
    for (let i = 0; i < acollection.length; i++) {
        acollection[i].style.color = "#0645ad";
    }
    const tablecollection = document.getElementsByTagName("table");
    for (let i = 0; i < tablecollection.length; i++) {
        tablecollection[i].style.color = "inherit";
        tablecollection[i].style.background = "white";
    }
    const licollection = document.getElementsByTagName("li");
    for (let i = 0; i < licollection.length; i++) {
        licollection[i].style.background = "white";
    }
    document.querySelector("html").style.filter = "invert(1)";
    let Newmedia = document.querySelectorAll("img, picture, video");
    Newmedia.forEach((mediaItem) => {
        mediaItem.style.filter = "invert(1)"
    })
})
var increasedcontrast = document.getElementById("increasedcontrast");
increasedcontrast.addEventListener("click", () => {
    document.querySelector("html").style.filter = "invert(0)";
    let media = document.querySelectorAll("img, picture, video");
    media.forEach((mediaItem) => {
        mediaItem.style.filter = "invert(1)"
    })
    document.querySelector("html").style.backgroundColor = "white";
    document.querySelector("body").style.backgroundColor = "white";
    document.querySelector("html").style.color= "inherit";
    document.querySelector("body").style.color= "inherit";
    document.querySelector("span").style.color= "inherit";
    const collection = document.getElementsByTagName("span");
    for (let i = 0; i < collection.length; i++) {
        collection[i].style.color = "inherit";
    }
    const divcollection = document.getElementsByTagName("div");
    for (let i = 0; i < divcollection.length; i++) {
        divcollection[i].style.color = "inherit";
        divcollection[i].style.background = "white";
    }
    const h1collection = document.getElementsByTagName("h1");
    for (let i = 0; i < h1collection.length; i++) {
        h1collection[i].style.color = "inherit";
    }
    const h2collection = document.getElementsByTagName("h2");
    for (let i = 0; i < h2collection.length; i++) {
        h2collection[i].style.color = "inherit";
    }
    const h3collection = document.getElementsByTagName("h3");
    for (let i = 0; i < h3collection.length; i++) {
        h3collection[i].style.color = "inherit";
    }
    const pcollection = document.getElementsByTagName("p");
    for (let i = 0; i < pcollection.length; i++) {
        pcollection[i].style.color = "inherit";
    }
    const acollection = document.getElementsByTagName("a");
    for (let i = 0; i < acollection.length; i++) {
        acollection[i].style.color = "#0645ad";
    }
    const tablecollection = document.getElementsByTagName("table");
    for (let i = 0; i < tablecollection.length; i++) {
        tablecollection[i].style.color = "inherit";
        tablecollection[i].style.background = "white";
    }
    const licollection = document.getElementsByTagName("li");
    for (let i = 0; i < licollection.length; i++) {
        licollection[i].style.background = "white";
    }
    document.querySelector("html").style.filter = "contrast(1.75)";
    let Newmedia = document.querySelectorAll("img, picture, video");
    Newmedia.forEach((mediaItem) => {
        mediaItem.style.filter = "contrast(1)"
    })
})
var invertedgreyscale = document.getElementById("invertedgreyscale");
invertedgreyscale.addEventListener("click", () => {
    document.querySelector("html").style.filter = "invert(0)";
    let media = document.querySelectorAll("img, picture, video");
    media.forEach((mediaItem) => {
        mediaItem.style.filter = "invert(0)"
    })
    document.querySelector("html").style.backgroundColor = "white";
    document.querySelector("body").style.backgroundColor = "white";
    document.querySelector("html").style.color= "inherit";
    document.querySelector("body").style.color= "inherit";
    document.querySelector("span").style.color= "inherit";
    const collection = document.getElementsByTagName("span");
    for (let i = 0; i < collection.length; i++) {
        collection[i].style.color = "inherit";
    }
    const divcollection = document.getElementsByTagName("div");
    for (let i = 0; i < divcollection.length; i++) {
        divcollection[i].style.color = "inherit";
        divcollection[i].style.background = "white";
    }
    const h1collection = document.getElementsByTagName("h1");
    for (let i = 0; i < h1collection.length; i++) {
        h1collection[i].style.color = "inherit";
    }
    const h2collection = document.getElementsByTagName("h2");
    for (let i = 0; i < h2collection.length; i++) {
        h2collection[i].style.color = "inherit";
    }
    const h3collection = document.getElementsByTagName("h3");
    for (let i = 0; i < h3collection.length; i++) {
        h3collection[i].style.color = "inherit";
    }
    const pcollection = document.getElementsByTagName("p");
    for (let i = 0; i < pcollection.length; i++) {
        pcollection[i].style.color = "inherit";
    }
    const acollection = document.getElementsByTagName("a");
    for (let i = 0; i < acollection.length; i++) {
        acollection[i].style.color = "#0645ad";
    }
    const tablecollection = document.getElementsByTagName("table");
    for (let i = 0; i < tablecollection.length; i++) {
        tablecollection[i].style.color = "inherit";
        tablecollection[i].style.background = "white";
    }
    const licollection = document.getElementsByTagName("li");
    for (let i = 0; i < licollection.length; i++) {
        licollection[i].style.background = "white";
    }
    document.querySelector("html").style.filter = "grayscale(1) invert(1.75)";
    let Newmedia = document.querySelectorAll("img, picture, video");
    Newmedia.forEach((mediaItem) => {
        mediaItem.style.filter = "grayscale(1) invert(1)"
    })
})
var yellowonblack = document.getElementById("yellowonblack");
yellowonblack.addEventListener("click", () => {
    document.querySelector("html").style.filter = "invert(0)";
    let media = document.querySelectorAll("img, picture, video");
    media.forEach((mediaItem) => {
        mediaItem.style.filter = "invert(0)"
    })
    document.querySelector("html").style.backgroundColor = "black";
    document.querySelector("body").style.backgroundColor = "black";
    document.querySelector("html").style.color= "yellow";
    document.querySelector("body").style.color= "yellow";
    document.querySelector("span").style.color= "yellow";
    const collection = document.getElementsByTagName("span");
    for (let i = 0; i < collection.length; i++) {
        collection[i].style.color = "yellow";
    }
    const divcollection = document.getElementsByTagName("div");
    for (let i = 0; i < divcollection.length; i++) {
        divcollection[i].style.color = "yellow";
        divcollection[i].style.background = "black";
    }
    const h1collection = document.getElementsByTagName("h1");
    for (let i = 0; i < h1collection.length; i++) {
        h1collection[i].style.color = "yellow";
    }
    const h2collection = document.getElementsByTagName("h2");
    for (let i = 0; i < h2collection.length; i++) {
        h2collection[i].style.color = "yellow";
    }
    const h3collection = document.getElementsByTagName("h3");
    for (let i = 0; i < h3collection.length; i++) {
        h3collection[i].style.color = "yellow";
    }
    const pcollection = document.getElementsByTagName("p");
    for (let i = 0; i < pcollection.length; i++) {
        pcollection[i].style.color = "yellow";
    }
    const acollection = document.getElementsByTagName("a");
    for (let i = 0; i < acollection.length; i++) {
        acollection[i].style.color = "white";
    }
    const tablecollection = document.getElementsByTagName("table");
    for (let i = 0; i < tablecollection.length; i++) {
        tablecollection[i].style.color = "yellow";
        tablecollection[i].style.background = "black";
    }
    const licollection = document.getElementsByTagName("li");
    for (let i = 0; i < licollection.length; i++) {
        licollection[i].style.background = "black";
    }
})

var fontStyle = document.getElementById("fonts");
    fontStyle.addEventListener("change", () => {
        var op = fontStyle.options[fontStyle.selectedIndex].text;
        if (op === 'Arial') {
            document.querySelector("body").style.fontFamily = 'Arial';
            const collection = document.getElementsByTagName("span");
            for (let i = 0; i < collection.length; i++) {
                collection[i].style.fontFamily = 'Arial';
            }
            const h3collection = document.getElementsByTagName("h3");
            for (let i = 0; i < h3collection.length; i++) {
                h3collection[i].style.fontFamily = 'Arial';
            }
            const acollection = document.getElementsByTagName("a");
            for (let i = 0; i < acollection.length; i++) {
                acollection[i].style.fontFamily = 'Arial';
            }
            const pcollection = document.getElementsByTagName("p");
            for (let i = 0; i < pcollection.length; i++) {
                pcollection[i].style.fontFamily = 'Arial';
            }
            const divcollection = document.getElementsByTagName("div");
            for (let i = 0; i < divcollection.length; i++) {
                divcollection[i].style.fontFamily = 'Arial';
            }
        }
        else if (op === 'Rockwell') {
            document.querySelector("body").style.fontFamily = 'Rockwell';
            const collection = document.getElementsByTagName("span");
            for (let i = 0; i < collection.length; i++) {
                collection[i].style.fontFamily = 'Rockwell';
            }
            const h3collection = document.getElementsByTagName("h3");
            for (let i = 0; i < h3collection.length; i++) {
                h3collection[i].style.fontFamily = 'Rockwell';
            }
            const acollection = document.getElementsByTagName("a");
            for (let i = 0; i < acollection.length; i++) {
                acollection[i].style.fontFamily = 'Rockwell';
            }
            const pcollection = document.getElementsByTagName("p");
            for (let i = 0; i < pcollection.length; i++) {
                pcollection[i].style.fontFamily = 'Rockwell';
            }
            const divcollection = document.getElementsByTagName("div");
            for (let i = 0; i < divcollection.length; i++) {
                divcollection[i].style.fontFamily = 'Rockwell';
            }
        }
        else if (op === 'Tahoma') {
            document.querySelector("body").style.fontFamily = 'Tahoma';
            const collection = document.getElementsByTagName("span");
            for (let i = 0; i < collection.length; i++) {
                collection[i].style.fontFamily = 'Tahoma';
            }
            const h3collection = document.getElementsByTagName("h3");
            for (let i = 0; i < h3collection.length; i++) {
                h3collection[i].style.fontFamily = 'Tahoma';
            }
            const acollection = document.getElementsByTagName("a");
            for (let i = 0; i < acollection.length; i++) {
                acollection[i].style.fontFamily = 'Tahoma';
            }
            const pcollection = document.getElementsByTagName("p");
            for (let i = 0; i < pcollection.length; i++) {
                pcollection[i].style.fontFamily = 'Tahoma';
            }
            const divcollection = document.getElementsByTagName("div");
            for (let i = 0; i < divcollection.length; i++) {
                divcollection[i].style.fontFamily = 'Tahoma';
            }
        }
        else if (op === 'Times New Roman') {
            document.querySelector("body").style.fontFamily = 'Times New Roman';
            const collection = document.getElementsByTagName("span");
            for (let i = 0; i < collection.length; i++) {
                collection[i].style.fontFamily = 'Times New Roman';
            }
            const h3collection = document.getElementsByTagName("h3");
            for (let i = 0; i < h3collection.length; i++) {
                h3collection[i].style.fontFamily = 'Times New Roman';
            }
            const acollection = document.getElementsByTagName("a");
            for (let i = 0; i < acollection.length; i++) {
                acollection[i].style.fontFamily = 'Times New Roman';
            }
            const pcollection = document.getElementsByTagName("p");
            for (let i = 0; i < pcollection.length; i++) {
                pcollection[i].style.fontFamily = 'Times New Roman';
            }
            const divcollection = document.getElementsByTagName("div");
            for (let i = 0; i < divcollection.length; i++) {
                divcollection[i].style.fontFamily = 'Times New Roman';
            }
        }
        else if (op === 'Verdana') {
            document.querySelector("body").style.fontFamily = 'Verdana';
            const collection = document.getElementsByTagName("span");
            for (let i = 0; i < collection.length; i++) {
                collection[i].style.fontFamily = 'Verdana';
            }
            const h3collection = document.getElementsByTagName("h3");
            for (let i = 0; i < h3collection.length; i++) {
                h3collection[i].style.fontFamily = 'Verdana';
            }
            const acollection = document.getElementsByTagName("a");
            for (let i = 0; i < acollection.length; i++) {
                acollection[i].style.fontFamily = 'Verdana';
            }
            const pcollection = document.getElementsByTagName("p");
            for (let i = 0; i < pcollection.length; i++) {
                pcollection[i].style.fontFamily = 'Verdana';
            }
            const divcollection = document.getElementsByTagName("div");
            for (let i = 0; i < divcollection.length; i++) {
                divcollection[i].style.fontFamily = 'Verdana';
            }
        }
    })

    var brightnessRange = document.getElementById("brightnessRange");
    brightnessRange.addEventListener("change", () => {
        var bval = brightnessRange.value;
        let st = bval.toString();
        var config = st;
        document.querySelector("html").style.filter = "brightness(" + config + "%)";
    })

    // var contrastRange = document.getElementById("contrastRange");
    // contrastRange.addEventListener("change", () => {
    //     document.querySelector("html").style.filter = "contrast(" + config + "%)";
    // })

    var fontRange = document.getElementById("fontRange");
    fontRange.addEventListener("change", () => {
        var fval = fontRange.value;
        let si = fval.toString();
        var config = si;
        document.querySelector("html").style.fontSize= "" + config + "px";
        document.querySelector("body").style.fontSize= "" + config + "px";
        document.querySelector("span").style.fontSize= "" + config + "px";
        const collection = document.getElementsByTagName("span");
        for (let i = 0; i < collection.length; i++) {
            collection[i].style.fontSize = "" + config + "px";
        }
        const divcollection = document.getElementsByTagName("div");
        for (let i = 0; i < divcollection.length; i++) {
            divcollection[i].style.fontSize = "" + config + "px";
        }
        const h3collection = document.getElementsByTagName("h3");
        for (let i = 0; i < h3collection.length; i++) {
            h3collection[i].style.fontSize = "" + config + "px";
        }
        const pcollection = document.getElementsByTagName("p");
        for (let i = 0; i < pcollection.length; i++) {
            pcollection[i].style.fontSize = "" + config + "px";
        }
    })

    const btnbg = document.querySelector(".btnbg");
    btnbg.addEventListener("click", () => {
        var backgroundColor = document.getElementById("backgroundColor").value;
        var bconfig = backgroundColor;
        document.querySelector("html").style.backgroundColor = bconfig;
        document.querySelector("body").style.backgroundColor = bconfig;
        const divcollection = document.getElementsByTagName("div");
        for (let i = 0; i < divcollection.length; i++) {
            divcollection[i].style.background = bconfig;
        }
        const tablecollection = document.getElementsByTagName("table");
        for (let i = 0; i < tablecollection.length; i++) {
            tablecollection[i].style.background = bconfig;
        }
        const licollection = document.getElementsByTagName("li");
        for (let i = 0; i < licollection.length; i++) {
            licollection[i].style.background = bconfig;
        }
    })
    
    const btntext = document.querySelector(".btntext");
    btntext.addEventListener("click", () => {
        var textColor = document.getElementById("textColor").value;
        var bconfig = textColor;
        document.querySelector("html").style.color= bconfig;
        document.querySelector("body").style.color= bconfig;
        document.querySelector("span").style.color= bconfig;
        const collection = document.getElementsByTagName("span");
        for (let i = 0; i < collection.length; i++) {
            collection[i].style.color = bconfig;
        }
        const divcollection = document.getElementsByTagName("div");
        for (let i = 0; i < divcollection.length; i++) {
            divcollection[i].style.color = bconfig;
        }
        const h1collection = document.getElementsByTagName("h1");
        for (let i = 0; i < h1collection.length; i++) {
            h1collection[i].style.color = bconfig;
        }
        const h2collection = document.getElementsByTagName("h2");
        for (let i = 0; i < h2collection.length; i++) {
            h2collection[i].style.color = bconfig;
        }
        const h3collection = document.getElementsByTagName("h3");
        for (let i = 0; i < h3collection.length; i++) {
            h3collection[i].style.color = bconfig;
        }
        const pcollection = document.getElementsByTagName("p");
        for (let i = 0; i < pcollection.length; i++) {
            pcollection[i].style.color = bconfig;
        }
        const acollection = document.getElementsByTagName("a");
        for (let i = 0; i < acollection.length; i++) {
            acollection[i].style.color = bconfig;
        }
        const tablecollection = document.getElementsByTagName("table");
        for (let i = 0; i < tablecollection.length; i++) {
            tablecollection[i].style.color = bconfig;
        }
    })