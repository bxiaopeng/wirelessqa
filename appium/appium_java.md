


## 测试JAVA用例：

### 1. 安装ContactManagers.spk: 

路径apps/ContactManager/ContactManagers.spk 

### 2. 打开用例到IntelliJ: 

Open --  选中appium/sample-code/examples/java/junit/pom.xml打开

### 3. 环境配置: 

如果依赖的jar包没有加载进来,可能需要配置maven的路径

### 4. 运行测试用例: 

右点选中AndroidContactsTest — Run'AndroidContactsTest'

## 用例欣赏:

```
package com.saucelabs.appium;

import io.appium.java_client.AppiumDriver;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.io.File;
import java.net.URL;
import java.util.List;

public class AndroidContactsTest {
    private AppiumDriver driver;

    @Before
    public void setUp() throws Exception {
        // set up appium
        File classpathRoot = new File(System.getProperty("user.dir"));
        File appDir = new File(classpathRoot, "../../../apps/ContactManager");
        File app = new File(appDir, "ContactManager.apk");
        DesiredCapabilities capabilities = new DesiredCapabilities();
        capabilities.setCapability("device","Android");
        capabilities.setCapability(CapabilityType.BROWSER_NAME, "");
        capabilities.setCapability(CapabilityType.VERSION, "4.4");
        capabilities.setCapability("app", app.getAbsolutePath());
        capabilities.setCapability("app-package", "com.example.android.contactmanager");
        capabilities.setCapability("app-activity", ".ContactManager");
        driver = new AppiumDriver(new URL("http://0.0.0.0:4723/wd/hub"), capabilities);
    }

    @After
    public void tearDown() throws Exception {
        driver.quit();
    }

    @Test
    public void addContact(){
        WebElement el = driver.findElement(By.name("Add Contact"));
        el.click();
        List<WebElement> textFieldsList = driver.findElementsByClassName("android.widget.EditText");
        textFieldsList.get(0).sendKeys("Some Name");
        textFieldsList.get(2).sendKeys("Some@example.com");
        //driver.swipe(100, 500, 100, 100, 2);
        driver.findElementByName("Save").click();
    }

}

```

## 二. 新建自己的测试工程

1. 步骤: New Project -- Maven -- 输入Project name -- Project location -- Next -- Next

2. 加入pom依赖


```
    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.11</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.seleniumhq.selenium</groupId>
            <artifactId>selenium-java</artifactId>
            <version>LATEST</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>io.appium</groupId>
            <artifactId>java-client</artifactId>
            <version>1.0.2</version>
        </dependency>
        <dependency>
            <groupId>com.googlecode.json-simple</groupId>
            <artifactId>json-simple</artifactId>
            <version>1.1</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>commons-lang</groupId>
            <artifactId>commons-lang</artifactId>
            <version>2.6</version>
            <scope>test</scope>
        </dependency>
        <!-- Includes the Sauce JUnit helper libraries -->
        <dependency>
            <groupId>com.saucelabs</groupId>
            <artifactId>sauce_junit</artifactId>
            <version>1.0.18</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>com.google.code.gson</groupId>
            <artifactId>gson</artifactId>
            <version>2.2.4</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
            </plugin>
            <plugin>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <source>1.5</source>
                    <target>1.5</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <repositories>
        <repository>
            <id>saucelabs-repository</id>
            <url>https://repository-saucelabs.forge.cloudbees.com/release</url>
            <releases>
                <enabled>true</enabled>
            </releases>
            <snapshots>
                <enabled>true</enabled>
            </snapshots>
        </repository>
    </repositories>
```


## 用例开始

```
package com.wirelessqa.android;

import io.appium.java_client.AppiumDriver;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;
import java.net.URL;
import java.util.concurrent.TimeUnit;

/**
 * Created by bixiaopeng on 14-5-13.
 */
public class appium {

    private AppiumDriver driver;


    @Before
    public void setUp() throws Exception {

        File classpathroot = new File(System.getProperty("user.dir"));
        File appDir = new File(classpathroot, "apk");
        File app = new File(appDir, "xiamimusic.apk");
        System.out.print(app.getAbsolutePath());
        DesiredCapabilities capabilities = new DesiredCapabilities();
        capabilities.setCapability(CapabilityType.BROWSER_NAME, "");
        capabilities.setCapability(CapabilityType.VERSION, "4.4");
        capabilities.setCapability("app", app.getAbsolutePath());
        capabilities.setCapability("app-package", "fm.xiami.main");
        capabilities.setCapability("app-activity", "fm.xiami.bmamba.activity.StartActivity");
        driver = new AppiumDriver(new URL("http://0.0.0.0:4723/wd/hub"), capabilities);

    }

    @Test
    public void login() throws Exception {
        //判断某个元素是否显示
        if (driver.findElement(By.name("是否创建桌面快捷方式")).isDisplayed()) {
            driver.findElement(By.name("确定")).click();
        }
        driver.findElement(By.name("我的音乐")).click();

        driver.findElementByName("点击头像登录").click();
        driver.findElementByName("虾米账户登录").click();
        //输入字符
        driver.findElementByName("输入邮箱地址").sendKeys("********");
        //通过id查找
        driver.findElement(By.id("fm.xiami.main:id/edit_password")).sendKeys("****");
        driver.findElementById("fm.xiami.main:id/btn_login").click();
        String userName = driver.findElementById("fm.xiami.main:id/user_name").getText();
        //断言
        assertEquals(userName, "老毕");

    }


    @After
    public void tearDown() throws Exception {
        driver.quit();
    }

}    
```


## 注意JDK版本的选择

Open Module Setting -- Language level: 5.0




## java例子参考

http://testerhome.com/topics/876

####  微信公众帐号: wirelessqa 
![wirelessqa](../img/qrcode_for_gh_fdde1fe2880a_258.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>